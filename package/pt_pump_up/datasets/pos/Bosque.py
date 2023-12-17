from pt_pump_up.datasets.Dataset import Dataset
from conllu import parse as conllu_parse
from datasets import Dataset as HF_Dataset
from datasets import DatasetDict
from tqdm import tqdm
import logging


class Bosque(Dataset):
    def __init__(self, repo_id) -> None:
        super().__init__(repo_id)

    def normalize(self, **kwargs):
        return kwargs["test_lines_conllu"] + "\n" + kwargs["test_blind_lines_conllu"]

    def parse(self):
        train_path = self.download(
            subfolder="raw",
            filename="portuguese_bosque_train.conll"
        )

        test_blind_path = self.download(
            subfolder="raw",
            filename="portuguese_bosque_test_blind.conll"
        )

        test_path = self.download(
            subfolder="raw",
            filename="portuguese_bosque_test.conll"
        )

        with open(train_path, "r", encoding="utf-8") as f:
            train_lines_conllu = f.read()

        with open(test_blind_path, "r", encoding="utf-8") as f:
            test_blind_lines_conllu = f.read()

        with open(test_path, "r", encoding="utf-8") as f:
            test_lines_conllu = f.read()

        test_lines_conllu = self.normalize(
            test_lines_conllu=test_lines_conllu, test_blind_lines_conllu=test_blind_lines_conllu)

        dataset_dict = DatasetDict()

        for split in [{"name": "train", "lines": train_lines_conllu}, {"name": "test", "lines": test_lines_conllu}]:

            logging.info(f"Parsing {split['name']}")

            dataset = {
                "tokens": [],
                "lemmas": [],
                "pos_tags": [],
            }

            for sentence in tqdm(conllu_parse(split["lines"])):

                accumulator = {
                    "tokens": [],
                    "lemmas": [],
                    "pos_tags": [],
                }

                for token in sentence:
                    accumulator["tokens"].append(token["form"])
                    accumulator["lemmas"].append(token["lemma"])
                    accumulator["pos_tags"].append(token["upos"])

                dataset["tokens"].append(accumulator["tokens"])
                dataset["lemmas"].append(accumulator["lemmas"])
                dataset["pos_tags"].append(accumulator["pos_tags"])

            dataset_dict[split["name"]] = HF_Dataset.from_dict(dataset)

            self.hf_dataset = dataset_dict

        return dataset_dict
