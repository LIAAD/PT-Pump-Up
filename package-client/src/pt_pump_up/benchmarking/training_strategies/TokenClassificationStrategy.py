import evaluate
from transformers import DataCollatorForTokenClassification, AutoModelForTokenClassification
from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
import numpy as np


class TokenClassificationStrategy(TrainingStrategy):
    def __init__(self, model_name, task, label_names, label_all_tokens: bool = False) -> None:
        super().__init__(model_name, label_names, "f1")

        id2label = {i: label for i, label in enumerate(label_names)}
        label2id = {v: k for k, v in id2label.items()}

        self.model = AutoModelForTokenClassification.from_pretrained(
            model_name, id2label=id2label, label2id=label2id)

        self.collator = DataCollatorForTokenClassification(
            tokenizer=self.tokenizer)
        self.metric = evaluate.load("seqeval")
        self.task = task
        self.label_all_tokens = label_all_tokens

    def align_labels_with_tokens(self, labels, word_ids):
        new_labels = []
        current_word = None
        for word_id in word_ids:
            if word_id != current_word:
                # Start of a new word!
                current_word = word_id
                label = -100 if word_id is None else labels[word_id]
                new_labels.append(label)
            elif word_id is None:
                # Special token
                new_labels.append(-100)
            else:
                # Same word as previous token
                label = labels[word_id]
                # If the label is B-XXX we change it to I-XXX
                if label % 2 == 1:
                    label += 1
                new_labels.append(label)

        return new_labels

    def prepare_data(self, examples):
        tokenized_inputs = self.tokenizer(
            examples["tokens"], truncation=True, is_split_into_words=True)

        all_labels = examples[f"{self.task.lower()}_tags"]

        new_labels = []

        for i, labels in enumerate(all_labels):
            word_ids = tokenized_inputs.word_ids(i)
            new_labels.append(self.align_labels_with_tokens(labels, word_ids))

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
