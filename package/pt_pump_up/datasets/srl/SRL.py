from tqdm import tqdm

TOKEN_IDX = 1


class SRL:
    def __init__(self, lines_conllu, index_offset, token_pos) -> None:
        self.accumulator = {}
        self.lines_conllu = lines_conllu
        self.index_offset = index_offset
        self.token_pos = token_pos

    def reinit_accumulator(self, line):
        number_verbs = len(line.split('\t')[self.index_offset:])

        self.accumulator = {
            'tokens': [],
            'srl_frames': [{'frames': [], 'stack': [], 'verb': None} for _ in range(number_verbs)]
        }

    def extract_label(self, tag):
        return tag.replace('(', '').replace(')', '').replace('*', '')

    def process_column(self, idx, tag):
        # Normalize tag
        tag = tag.strip()

        # Process * tag
        if tag == '*' and self.accumulator['srl_frames'][idx]['stack'] == []:
            return 'O'

        elif tag == '*' and self.accumulator['srl_frames'][idx]['stack'] != []:
            return f"I-{self.accumulator['srl_frames'][idx]['stack'][-1]}"

        # Process Tags with (
        if tag.startswith('(') and not tag.endswith(')'):
            label = self.extract_label(tag)
            self.accumulator['srl_frames'][idx]['stack'].append(label)
            return f"B-{label}"

        # Single Token label is not worth placing in stack
        elif tag.startswith('(') and tag.endswith(')'):
            return f"B-{self.extract_label(tag)}"

        # Process Tags with )
        if tag.endswith(')'):
            label = self.accumulator['srl_frames'][idx]['stack'][-1]
            self.accumulator['srl_frames'][idx]['stack'].pop()
            return f"I-{label}"

    def process_line(self, line):
       srl_tags = line.split('\t')[self.index_offset:]

       self.accumulator['tokens'].append(
           line.split('\t')[self.token_pos].strip())

       for idx, tag in enumerate(srl_tags):
           tag = self.process_column(idx, tag)

           self.accumulator['srl_frames'][idx]['frames'].append(tag)

           # Fill Verb Information
           if tag == 'B-V':
               self.accumulator['srl_frames'][idx]['verb'] = line.split('\t')[
                   self.token_pos].strip()

    def validate_stack(self):
        for srl_frame in self.accumulator['srl_frames']:
            if srl_frame['stack'] != []:
                return False

        return True

    def parse_conllu(self):
        sentences = []

        for line in tqdm(self.lines_conllu):

            if self.accumulator == {}:
                self.reinit_accumulator(line)

            if line == '':
                raise Exception("Empty line found. Only \ n is allowed")

            if line == '\n':
                sentences.append(self.accumulator)

                # Validate Stack. In a Pushdown Automata, the stack must be empty at the end of the process
                # If not, there is a problem with the input
                if not self.validate_stack():
                    raise Exception("Stack not empty")

                self.accumulator = {}

                continue

            self.process_line(line)

        return sentences
