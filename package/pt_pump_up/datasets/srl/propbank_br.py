from huggingface_hub import hf_hub_download
from pt_pump_up.datasets.Dataset import Dataset as PTPumpUpDataset
from datasets import Dataset as HFDataset
import bs4 as bs
import os
import pandas as pd
from tqdm import tqdm
import numpy as np


class PropbankBr(PTPumpUpDataset):
    def __init__(self, hf_token=None) -> None:
        super().__init__("liaad/Propbank-BR", os.path.join("raw"),
                         "PropBank.Br_short.xml", hf_token)

    def standardize(self) -> HFDataset:
        pass

propbank_br = PropbankBr()

dataset = propbank_br.standardize()

print(dataset)

# propbank_br.publish(dataset)
