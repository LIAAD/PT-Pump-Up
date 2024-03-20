import evaluate
from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
from transformers import AutoModelForSequenceClassification, DataCollatorWithPadding
import numpy as np


class TextClassificationStrategy(TrainingStrategy):
    def __init__(self, model_name) -> None:
        super().__init__(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name)
        self.collator = DataCollatorWithPadding(tokenizer=self.tokenizer)
        self.metric = evaluate.load("accuracy")

    def prepare_data(self, examples):
        return examples

    def compute_metrics(self, eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)
        return self.metric.compute(predictions=predictions, references=labels)
