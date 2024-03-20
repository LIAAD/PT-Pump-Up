import evaluate
from transformers import DataCollatorForTokenClassification, AutoModelForTokenClassification
from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
import numpy as np


class TokenClassificationStrategy(TrainingStrategy):
    def __init__(self, model_name, task, label_names, label_all_tokens: bool = False) -> None:
        super().__init__(model_name, label_names, "f1")

        self.model = AutoModelForTokenClassification.from_pretrained(
            model_name, num_labels=len(label_names))

        self.collator = DataCollatorForTokenClassification(
            tokenizer=self.tokenizer)
        self.metric = evaluate.load("seqeval")
        self.task = task
        self.label_all_tokens = label_all_tokens

    def prepare_data(self, examples):
        tokenized_inputs = self.tokenizer(
            examples["tokens"], truncation=True, is_split_into_words=True, max_length=self.model.config.max_position_embeddings)

        labels = []
        for i, label in enumerate(examples[f"{self.task}_tags"]):
            word_ids = tokenized_inputs.word_ids(batch_index=i)
            previous_word_idx = None
            label_ids = []
            for word_idx in word_ids:
                # Special tokens have a word id that is None. We set the label to -100 so they are automatically
                # ignored in the loss function.
                if word_idx is None:
                    label_ids.append(-100)
                # We set the label for the first token of each word.
                elif word_idx != previous_word_idx:
                    label_ids.append(label[word_idx])
                # For the other tokens in a word, we set the label to either the current label or -100, depending on
                # the label_all_tokens flag.
                else:
                    label_ids.append(
                        label[word_idx] if self.label_all_tokens else -100)
                previous_word_idx = word_idx

            labels.append(label_ids)

        tokenized_inputs["labels"] = labels

        return tokenized_inputs

    def compute_metrics(self, eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=2)

        # Remove ignored index (special tokens)
        true_predictions = [
            [self.label_names[p]
                for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]
        true_labels = [
            [self.label_names[l]
                for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]

        results = self.metric.compute(
            predictions=true_predictions, references=true_labels)
        return {
            "precision": results["overall_precision"],
            "recall": results["overall_recall"],
            "f1": results["overall_f1"],
            "accuracy": results["overall_accuracy"],
        }
