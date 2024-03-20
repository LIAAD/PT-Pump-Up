import os
from transformers import Trainer, TrainingArguments, EarlyStoppingCallback
from pt_pump_up import PTPumpUpClient
from pt_pump_up.benchmarking.training_strategies import TokenClassificationStrategy, TextClassificationStrategy


class TrainerFactory:
    @staticmethod
    def create(nlp_task: str, repository_name: str, model_name: str, lr: float, max_epochs: int, train_dataset, eval_dataset=None):
        strategy = None
        nlp_tasks = PTPumpUpClient().all_nlp_tasks()

        nlp_task = nlp_tasks[nlp_tasks['short_name'] == nlp_task].to_dict('records')[
            0]

        if nlp_task is None:
            raise Exception("NLP Task not found")

        if nlp_task['standard_format'] == 'Token Classification':
            strategy = TokenClassificationStrategy(
                model_name, nlp_task['short_name'].lower(), train_dataset.features[f"{nlp_task['short_name'].lower()}_tags"].feature.names)

        elif nlp_task['standard_format'] == 'Text Classification':
            strategy = TextClassificationStrategy(
                model_name, train_dataset.features['label'].feature.names)

        elif nlp_task['standard_format'] == 'Question Answering':
            raise Exception("Not implemented")
        elif nlp_task['standard_format'] == 'Summarization':
            raise Exception("Not implemented")
        elif nlp_task['standard_format'] == 'Translation':
            raise Exception("Not implemented")
        elif nlp_task['standard_format'] == 'Text Generation':
            raise Exception("Not implemented")
        elif nlp_task['standard_format'] == 'Sentence Similarity':
            raise Exception("Not implemented")
        else:
            raise Exception("Strategy not found for NLP Task")

        args = TrainingArguments(
            output_dir=os.path.join(os.getcwd(), 'output'),
            evaluation_strategy="epoch",
            learning_rate=lr,
            save_strategy="epoch",
            auto_find_batch_size=True,
            num_train_epochs=max_epochs,
            load_best_model_at_end=True,
            metric_for_best_model=strategy.metric_for_best_model,
            hub_model_id=repository_name,
            label_names=strategy.label_names,
            bf16=True,
            push_to_hub=True,
        )

        # PreProcessing Data
        train_dataset = train_dataset.map(strategy.prepare_data, batched=True)
        eval_dataset = eval_dataset.map(
            strategy.prepare_data, batched=True) if eval_dataset else None

        # Create Trainer
        return Trainer(
            model=strategy.model,
            args=args,
            compute_metrics=strategy.compute_metrics,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            data_collator=strategy.collator,
            tokenizer=strategy.tokenizer,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]
        )
