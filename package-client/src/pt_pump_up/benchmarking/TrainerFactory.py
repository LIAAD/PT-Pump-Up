import os
from transformers import Trainer
from transformers import TrainingArguments
from pt_pump_up import PTPumpUpClient
from pt_pump_up.benchmarking.training_strategies import TokenClassificationStrategy, TextClassificationStrategy


class TrainerFactory:
    @staticmethod
    def create(nlp_task: str, repository_name: str, model_name: str, lr: float, batch_size: int, max_epochs: int, train_dataset, eval_dataset=None):
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
            strategy = TextClassificationStrategy()

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
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            num_train_epochs=max_epochs,
            load_best_model_at_end=True,
            hub_model_id=repository_name,
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
        )
