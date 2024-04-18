import evaluate
import nltk
import numpy as np
from pt_pump_up.benchmarking.training_strategies.TrainingStrategy import TrainingStrategy
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from nltk.tokenize import sent_tokenize

nltk.download("punkt")


class AbstractiveTextSummarizationStrategy(TrainingStrategy):
    def __init__(self, model_name, metric_for_best_model="rougeL") -> None:
        super().__init__(model_name, None, metric_for_best_model)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.collator = DataCollatorForSeq2Seq(
            tokenizer=self.tokenizer, model=self.model)
        self.rouge_score = evaluate.load("rouge")

    def prepare_data(self, examples, **kwargs):
        # title_column_name = kwargs.get("title_column_name", "title")
        text_column_name = kwargs.get("text_column_name", "text")
        summary_column_name = kwargs.get("summary_column_name", "summary")

        summary_target_length = kwargs.get("summary_target_length", 128)

        tokenized_inputs = self.tokenizer(
            examples[text_column_name],
            max_length=self.model.config.max_position_embeddings,
            padding="longest",
            truncation=True,
            return_tensors="pt",
        )

        labels = self.tokenizer(
            examples[summary_column_name],
            max_length=summary_target_length,
            padding="longest",
            truncation=True,
            return_tensors="pt",
        )

        tokenized_inputs["labels"] = labels["input_ids"]

        return tokenized_inputs

    def compute_metrics(self, eval_pred):
        predictions, labels = eval_pred
        # Decode generated summaries into text
        decoded_preds = self.tokenizer.batch_decode(
            predictions, skip_special_tokens=True)
        # Replace -100 in the labels as we can't decode them
        labels = np.where(labels != -100, labels, self.tokenizer.pad_token_id)
        # Decode reference summaries into text
        decoded_labels = self.tokenizer.batch_decode(
            labels, skip_special_tokens=True)
        # ROUGE expects a newline after each sentence
        decoded_preds = ["\n".join(sent_tokenize(pred.strip()))
                         for pred in decoded_preds]
        decoded_labels = ["\n".join(sent_tokenize(label.strip()))
                          for label in decoded_labels]
        # Compute ROUGE scores
        result = self.rouge_score.compute(
            predictions=decoded_preds, references=decoded_labels, use_stemmer=True
        )
        # Extract the median scores
        result = {key: value.mid.fmeasure *
                  100 for key, value in result.items()}
        return {k: round(v, 4) for k, v in result.items()}
