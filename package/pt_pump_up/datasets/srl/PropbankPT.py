from pt_pump_up.datasets.Dataset import Dataset
import os
from pt_pump_up.datasets.srl.SRL import SRL
from bs4 import BeautifulSoup
from tqdm import tqdm
import tempfile
import logging
import re
import pandas as pd
from datasets import Dataset as HF_Dataset


class PropbankPT(Dataset):
    def __init__(self, hf_token) -> None:
        super().__init__(repo_id="liaad/Propbank-PT", hf_token=hf_token)
        self.INDEX_OFFSET = 9
        self.VERB_INDEX = 2

    def process_verbs(self, line, verb_counter):
        line_exploded = line.split('\t')
        line_exploded[self.INDEX_OFFSET-2+verb_counter] = "(V*)"

        return '\t'.join(line_exploded)

    def normalize(self, **kwargs):

        with open(kwargs['local_path'], "r", encoding="utf-8") as f:
            xml = f.read()

        soup = BeautifulSoup(xml, 'xml')

        conll = soup.find_all('conll')

        with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding="utf-8") as f:
            # Parse parse_conllu requires a file pointer
            logging.info(f"Creating temporary file at {f}")

            for elem in tqdm(conll):
                sentence = elem.text.strip()

                verb_counter = 0

                for line in sentence.split('\n'):

                    if line != '\n':
                        # Remove extra spaces from within a line
                        line = line.replace('\t', '')
                        line = re.sub(r'\s+', '\t', line).strip()

                        """
                        In PropbankPT, unlike PropbankBR and Propbank (English), the verbs are not marked with a 'V' in SRL column.
                        """
                        if line.split('\t')[self.VERB_INDEX] == 'V':
                            line = self.process_verbs(line, verb_counter)
                            verb_counter += 1

                        # f.tell() adds an id to each line
                        line = f"{f.tell()}'\t'{line}\n"

                    f.write(line)

                f.write('\n')

        return f

    def parse(self):
        local_path = self.download(
            # HF is Linux based. It is necessary to Force using forward slash To run on Windows Locals
            subfolder=os.path.join("raw"),
            filename="WSJ-Propbank.xml"
        )

        f = self.normalize(local_path=local_path)

        sentences = SRL().parse_conllu(fp=f.name, index_offset=self.INDEX_OFFSET)

        dataset = pd.DataFrame(data=sentences, columns=[
                               "tokens", "srl_frames"])

        self.hf_dataset = HF_Dataset.from_pandas(dataset)

        return self.hf_dataset