from datasets import load_dataset as hf_load_dataset
import logging
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from tqdm import tqdm


class HuggingFaceDataset:
    def __init__(self, dataset_name, textual_column_name, textual_column_tokenized=False) -> None:
        self.dataset_name = dataset_name
        self.textual_column_name = textual_column_name
        self.textual_column_tokenized = textual_column_tokenized
        self.dataset = None

    def load_dataset(self, *args, **kwargs):
        self.dataset = hf_load_dataset(self.dataset_name, *args, **kwargs)

        return self.dataset

    def produce_stats(self):
        if self.dataset is None:
            logging.warning(
                "Dataset is not loaded yet. Trying to load it without arguments")
            self.load_dataset()
            logging.info("Dataset loaded")

        number_of_rows = len(self.dataset)
        number_tokens = 0
        number_sentences = 0
        number_characters = 0

        for row in tqdm(self.dataset):

            if self.textual_column_tokenized:
                number_tokens += len(row[self.textual_column_name])
                number_characters += sum([len(token)
                                         for token in row[self.textual_column_name]])
                number_sentences += row[self.textual_column_name].count('.')
            else:
                number_tokens += len(word_tokenize(
                    row[self.textual_column_name]))
                number_characters += len(row[self.textual_column_name])
                number_sentences += len(sent_tokenize(
                    row[self.textual_column_name]))

        return number_of_rows, number_tokens, number_sentences, number_characters


class HuggingFaceModel:
    pass
