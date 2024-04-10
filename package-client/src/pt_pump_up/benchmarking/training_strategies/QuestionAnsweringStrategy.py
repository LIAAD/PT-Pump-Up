from pt_pump_up.benchmarking.training_strategies import TrainingStrategy
from pt_pump_up.benchmarking.training_strategies.utils import post_process_training_question_answering, post_process_validation_question_answering
from transformers import AutoModelForQuestionAnswering, DefaultDataCollator


class QuestionAnsweringStrategy(TrainingStrategy):
    def __init__(self, model_name) -> None:
        super().__init__(model_name, None, None)
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        self.collator = DefaultDataCollator()

    def prepare_data(self, examples, **kwargs):
        context_column_name = kwargs.get("context_column_name", "context")
        question_column_name = kwargs.get("question_column_name", "question")
        answers_column_name = kwargs.get("answers_column_name", "answers")
        stride = kwargs.get("stride", 50)

        tokenized_inputs = self.tokenizer(
            [q.strip() for q in examples[question_column_name]],
            examples[context_column_name],
            truncation="only_second",
            stride=stride,
            return_offsets_mapping=True,
            padding="max_length",
            max_length=self.model.config.max_position_embeddings,
        )

        start_positions, end_positions = post_process_training_question_answering(
            tokenized_inputs=tokenized_inputs,
            answers=examples[answers_column_name],
        )

        tokenized_inputs["start_positions"] = start_positions
        tokenized_inputs["end_positions"] = end_positions

        return tokenized_inputs

    def compute_metrics(self, eval_pred):
        return None
