from pt_pump_up.benchmarking import TrainerFactory
from datasets import load_dataset

squad_pt = load_dataset("squad_v1_pt")

for model_name in ["unicamp-dl/ptt5-small-t5-vocab", "unicamp-dl/ptt5-base-t5-vocab"]:

    trainer = TrainerFactory.create(
        nlp_task="Question Answering",
        repository_name=f"liaad/QA_{model_name.split('/')[1]}".replace(
            "-", "_"),
        model_name=model_name,
        max_epochs=30,
        lr=1e-5,
        train_dataset=squad_pt['train'],
        eval_dataset=squad_pt['validation'],
    )

    trainer.train()
