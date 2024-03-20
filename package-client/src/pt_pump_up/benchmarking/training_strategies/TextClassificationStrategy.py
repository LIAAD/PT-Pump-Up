import evaluate
from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
from transformers import AutoModelForSequenceClassification, DataCollatorWithPadding
import numpy as np


class TextClassificationStrategy(TrainingStrategy):
    def __init__(self, model_name, label_names) -> None:
        super().__init__(model_name, label_names, "accuracy")

        id2label = {i: label for i, label in enumerate(label_names)}
        label2id = {v: k for k, v in id2label.items()}

        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name, id2label=id2label, label2id=label2id)
        
        self.collator = DataCollatorWithPadding(tokenizer=self.tokenizer)
        self.metric = evaluate.load("accuracy")

    def prepare_data(self, examples):
        return self.tokenizer(examples["text"], 
                              truncation=True, 
                              max_length=self.model.config.max_position_embeddings)

    def compute_metrics(self, eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)
        return self.metric.compute(predictions=predictions, references=labels)
