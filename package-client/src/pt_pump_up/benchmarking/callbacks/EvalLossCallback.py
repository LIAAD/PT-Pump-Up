from transformers import TrainerCallback
from transformers.trainer_callback import TrainerControl, TrainerState
from transformers.training_args import TrainingArguments


class EvalLossCallback(TrainerCallback):
    def on_evaluate(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):        
        eval_loss = state.log_history[-1]['eval_loss']
        eval_f1 = state.log_history[-1]['eval_f1']

        if eval_loss < 0.1 and eval_f1 > 0.9:
            control.should_training_stop = True
            print("Stopping training")
        else:
            print(f"Eval loss: {eval_loss}, F1: {eval_f1} | Continue training.")