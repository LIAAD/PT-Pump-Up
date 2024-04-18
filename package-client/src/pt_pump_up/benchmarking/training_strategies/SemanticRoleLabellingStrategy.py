import evaluate
from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
from transformers import AutoModelForTokenClassification, DataCollatorForTokenClassification
from pt_pump_up.benchmarking.training_strategies.utils import align_labels_with_tokens
import numpy as np
from transformers.pipelines import PIPELINE_REGISTRY
from pt_pump_up.benchmarking.pipelines.srl import SRLPipeline
from transformers import AutoModelForTokenClassification
from transformers import pipeline
from huggingface_hub import Repository


class SemanticRoleLabellingStrategy(TrainingStrategy):
    def __init__(self, model_name, label_names, metric_for_best_model="f1") -> None:
        super().__init__(model_name, label_names, metric_for_best_model=metric_for_best_model)

        self.model = AutoModelForTokenClassification.from_pretrained(
            model_name, id2label=self.id2label, label2id=self.label2id, num_labels=len(self.label_names))

        self.collator = DataCollatorForTokenClassification(
            tokenizer=self.tokenizer)

        self.metric = evaluate.load("seqeval")

    def prepare_data(self, examples, **kwargs):
        # examples["verb"] is a string, so we need to convert it to a list
        examples["verb"] = [[verb] for verb in examples["verb"]]

        tokenized_inputs = self.tokenizer(
            examples["tokens"],
            examples["verb"],
            truncation=True,
            is_split_into_words=True,
            padding="longest",
            max_length=self.model.config.max_position_embeddings,
            return_tensors="pt"
        )

        return align_labels_with_tokens(
            tokenized_inputs, examples["frames"])

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

    @staticmethod
    def create_pipeline(hf_repo, model, tokenizer):
        PIPELINE_REGISTRY.register_pipeline(
            "srl",
            pipeline_class=SRLPipeline,
            pt_model=AutoModelForTokenClassification
        )
        pipe = pipeline("srl", model=model, tokenizer=tokenizer)

        repo = Repository(hf_repo, clone_from=hf_repo)

        pipe.save_pretrained(hf_repo)

        repo.push_to_hub(auto_lfs_prune=True)
