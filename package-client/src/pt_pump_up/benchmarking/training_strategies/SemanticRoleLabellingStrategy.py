import evaluate
from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
from transformers import AutoModelForTokenClassification, DataCollatorForTokenClassification
from pt_pump_up.benchmarking.training_strategies.utils import align_labels_with_tokens
import numpy as np


class SemanticRoleLabellingStrategy(TrainingStrategy):
    def __init__(self, model_name, label_names) -> None:
        super().__init__(model_name, label_names, metric_for_best_model="f1")
        self.model = AutoModelForTokenClassification.from_pretrained(
            model_name, id2label=self.id2label, label2id=self.label2id)
        self.collator = DataCollatorForTokenClassification(
            tokenizer=self.tokenizer)
        self.metric = evaluate.load("seqeval")

    def prepare_data(self, examples):
        # examples["verb"] is a string, so we need to convert it to a list
        examples["verb"] = [[verb] for verb in examples["verb"]]

        tokenized_inputs = self.tokenizer(
            examples["tokens"],
            examples["verb"],
            truncation=True,
            is_split_into_words=True,
            max_length=self.model.config.max_position_embeddings
        )

        all_labels = examples["frames"]

        new_labels = []

        for i, labels in enumerate(all_labels):
            word_ids = tokenized_inputs.word_ids(i)
            type_ids = tokenized_inputs[i].type_ids
            new_labels.append(align_labels_with_tokens(
                labels, word_ids, type_ids))

        tokenized_inputs["labels"] = new_labels

        return tokenized_inputs

    def compute_metrics(self, eval_pred):
        logits, labels = eval_pred

        predictions = np.argmax(logits, axis=-1)

        # Remove ignored index (special tokens) and convert to labels
        true_labels = [[self.label_names[l]
                        for l in label if l != -100] for label in labels]
        true_predictions = [
            [self.label_names[p]
                for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]

        all_metrics = self.metric.compute(
            predictions=true_predictions, references=true_labels)

        return {
            "precision": all_metrics["overall_precision"],
            "recall": all_metrics["overall_recall"],
            "f1": all_metrics["overall_f1"],
            "accuracy": all_metrics["overall_accuracy"],
        }