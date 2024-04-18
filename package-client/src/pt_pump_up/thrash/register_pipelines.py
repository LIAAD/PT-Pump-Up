from pt_pump_up.benchmarking.training_strategies.SemanticRoleLabellingStrategy import SemanticRoleLabellingStrategy
from transformers import AutoModel, AutoTokenizer
from transformers import pipeline

for model_name in ["liaad/propbank_br_srl_bert_base_portuguese_cased", "liaad/propbank_br_srl_bert_large_portuguese_cased", "liaad/propbank_br_srl_albertina_100m_portuguese_ptpt_encoder", "liaad/propbank_br_srl_albertina_900m_portuguese_ptpt_encoder"]:

    pipe = pipeline(model=model_name, trust_remote_code=True)

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, add_prefix_space=True)

    SemanticRoleLabellingStrategy.create_pipeline(
        hf_repo=model_name, model=pipe.model, tokenizer=tokenizer)
