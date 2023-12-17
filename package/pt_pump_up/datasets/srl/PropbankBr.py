from pt_pump_up.datasets.Dataset import Dataset
import os
from pt_pump_up.datasets.srl.SRL import SRL
import pandas as pd
from datasets import Dataset as HF_Dataset


class PropbankBr(Dataset):
    def __init__(self, hf_token) -> None:
        super().__init__(repo_id="liaad/Propbank-BR", hf_token=hf_token)

    def normalize(self, **kwargs):
        return super().normalize(**kwargs)

    def parse(self):

        local_path = self.download(
            subfolder=os.path.join("raw", "propbank_1.1"),
            filename="PropBankBr_v1.1_Const.conll"
        )
        with open(local_path, "r", encoding="utf-8") as f:
            lines_conllu = f.readlines()
            srl_parser = SRL(lines_conllu, index_offset=10, token_pos=1)

            sentences = srl_parser.parse_conllu()

            dataset = pd.DataFrame(data=sentences, columns=[
                "tokens", "srl_frames"])

            self.hf_dataset = HF_Dataset.from_pandas(dataset)

            return self.hf_dataset