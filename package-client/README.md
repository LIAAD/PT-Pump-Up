# PT Pump Up Client

## Use Cases

### Train Semantic Role Labeller

```python

from pt_pump_up.benchmarking import TrainerFactory
from pt_pump_up.benchmarking.training_strategies.SemanticRoleLabellingStrategy import SemanticRoleLabellingStrategy
from datasets import load_dataset

propbank_br = load_dataset("liaad/Propbank-BR", "flatten")

for model_name in ['neuralmind/bert-base-portuguese-cased', 'neuralmind/bert-large-portuguese-cased', 'PORTULAN/albertina-100m-portuguese-ptpt-encoder' 'PORTULAN/albertina-900m-portuguese-ptpt-encoder']:

    repository_name = f"SRL-{model_name.split('/')[1]}"

    trainer = TrainerFactory.create(
        nlp_task="SRL",
        repository_name=repository_name,
        model_name=model_name,
        max_epochs=30,
        lr=1e-5,
        train_dataset=propbank_br['train'],
        eval_dataset=propbank_br['test'],
    )

    trainer.train()

    SemanticRoleLabellingStrategy.create_pipeline(
        hf_repo=repository_name,
        model=trainer.model,
        tokenizer=trainer.tokenizer,
    )


```