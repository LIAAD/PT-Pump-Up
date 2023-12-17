from pt_pump_up.datasets.Dataset import Dataset
import os
from pt_pump_up.datasets.srl.SRL import SRL
from bs4 import BeautifulSoup
import re


class PropbankPT(Dataset):
    def __init__(self, hf_token) -> None:
        super().__init__(repo_id="liaad/Propbank-PT", hf_token=hf_token)

    def process_verbs(self, line, verb_counter):
        line_exploded = line.split('\t')
        line_exploded[self.INDEX_OFFSET-2+verb_counter] = "(V*)"

        return '\t'.join(line_exploded)

    def normalize(self, **kwargs):

        with open(kwargs['local_path'], "r", encoding="utf-8") as f:
            xml = f.read()

        soup = BeautifulSoup(xml, 'xml')

        str_all_conll = ''

        for idx, conll in enumerate(soup.find_all('conll')):

            text_formated = conll.get_text().strip()

            for line in text_formated.split('\n'):

                if line == '':
                    continue

                line = line.strip()

                line = line.replace('\t', '')

                line = re.sub(r'\s+', '\t', line).strip()

                str_all_conll += line + '\n'

            # TODO: Solve this problem. Empty String is not a native type in Propbank English
            if line == '':
                raise Exception("Empty line found")
            break

        return str_all_conll.split('\n')

    def parse(self):
        raise Exception(
            "This dataset is not ready yet. It has problems with the annotations. Authors of the dataset were contacted. Please, wait for a new version.")

        local_path = self.download(
            subfolder=os.path.join("raw"),
            filename="WSJ-Propbank.xml"
        )

        lines_conllu = self.normalize(local_path=local_path)

        srl_parser = SRL(lines_conllu, index_offset=7, token_pos=0)

        sentences = srl_parser.parse_conllu()

        """
        dataset = pd.DataFrame(data=sentences, columns=[
                               "tokens", "srl_frames"])

        self.hf_dataset = HF_Dataset.from_pandas(dataset)
        
        return self.hf_dataset
        """