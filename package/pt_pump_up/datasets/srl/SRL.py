from tqdm import tqdm

class SRL:

    @staticmethod
    def process_column(line, column, idx, accumulator):

        TOKEN_POS = 1

        def get_tag(column):

            if column == "*":
                return "O"

            return column.replace("(", "").replace(")", "").replace("*", "")

        if len(accumulator) <= idx:
            accumulator.append({
                'verb': None,
                'frames': [],
                'current_tag': None,
            })

        if column == "(V*)":
            tag = get_tag(column)

            accumulator[idx]['verb'] = line.split("\t")[TOKEN_POS].strip()
            accumulator[idx]['frames'].append(f"B-{tag}")

        elif column.startswith("("):
            tag = get_tag(column)

            accumulator[idx]['frames'].append(f"B-{tag}")
            accumulator[idx]['current_tag'] = tag

        elif column.endswith(")"):
            accumulator[idx]['frames'].append(
                f"I-{accumulator[idx]['current_tag']}")
            accumulator[idx]['current_tag'] = None

        elif column == "*" and accumulator[idx]['current_tag']:
            accumulator[idx]['frames'].append(
                f"I-{accumulator[idx]['current_tag']}")

        elif column == "*":
            tag = get_tag(column)

            accumulator[idx]['frames'].append(tag)

        else:
            raise Exception(f"Unknown column {column}")

        return accumulator

    @staticmethod
    def parse_conllu(fp, index_offset):

        def reset_accumulator():
            return {
                'tokens': [],
                'srl_frames': []
            }

        def clean_columns(accumulator):
            for verb in accumulator['srl_frames']:
                del verb['current_tag']

            return accumulator

        sentences = []

        with open(fp, "r", encoding="utf-8") as f:
            lines = f.readlines()

        accumulator = reset_accumulator()

        for line in tqdm(lines):

            # If \n line is found, it means that the sentence has ended
            # Reset the accumulator and start a new sentence
            if line == "\n":
                sentences.append(clean_columns(accumulator))
                accumulator = reset_accumulator()
                continue

            # Skip Non SRL columns in each line
            # Number of columns SRL is variable, and is equal to the number of verbs in the sentence
            for idx, column in enumerate(line.split("\t")[index_offset-1:]):
                SRL.process_column(line, column.strip(), idx,
                                   accumulator['srl_frames'])

            # Append token to the accumulator
            accumulator['tokens'].append(line.split("\t")[1].strip())

        return sentences
