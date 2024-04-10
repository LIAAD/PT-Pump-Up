import evaluate
from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
from transformers import AutoModelForSequenceClassification, DataCollatorWithPadding
import numpy as np


class TextClassificationStrategy(TrainingStrategy):
    def __init__(self, model_name, label_names, metric_for_best_model="f1") -> None:
        super().__init__(model_name, label_names, metric_for_best_model=metric_for_best_model)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name, id2label=self.id2label, label2id=self.label2id)

        self.collator = DataCollatorWithPadding(tokenizer=self.tokenizer)

        self.accuracy = evaluate.load("accuracy")
        self.f1 = evaluate.load("f1")
        self.precision = evaluate.load("precision")
        self.recall = evaluate.load("recall")

    def prepare_data(self, examples, **kwargs):
        return self.tokenizer(examples["text"],
                              truncation=True,
                              padding="longest",
                              max_length=self.model.config.max_position_embeddings,
                              return_tensors="pt")

    def compute_metrics(self, eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)

        return {
            "accuracy": self.accuracy.compute(predictions=predictions, references=labels)['accuracy'],
            "f1": self.f1.compute(predictions=predictions, references=labels)['f1'],
            "precision": self.precision.compute(predictions=predictions, references=labels)['precision'],
            "recall": self.recall.compute(predictions=predictions, references=labels)['recall']
        }
