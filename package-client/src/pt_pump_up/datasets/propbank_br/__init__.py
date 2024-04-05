import os
from tqdm import tqdm
from datasets import Dataset, DatasetDict, Features, ClassLabel, Sequence, Value

FILEPATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "data", "PBrConst.conll")


def extract_srl_tags(srl_tag):
    return srl_tag.replace("(", "").replace(")", "").replace("*", "").strip()


def reset_document():
    return {
        "tokens": [],
        "srl_frames": []
    }


def get_top_stack(stack):
    if len(stack) == 0:
        return None

    return stack[-1]


def flatten_dataset(dataset_dict, unique_labels):

    for split in dataset_dict.keys():
        dataset = dataset_dict[split]
        new_dataset = []

        for row in dataset:
            for srl_frame in row["srl_frames"]:
                new_dataset.append({
                    "tokens": row["tokens"],
                    "verb": srl_frame["verb"],
                    "frames": srl_frame["frames"]
                })

        dataset_dict[split] = Dataset.from_list(new_dataset, split=split, features=Features({
            "tokens": Sequence(Value('string')),
            "verb": Value('string'),
            "frames": Sequence(feature=ClassLabel(names=sorted(list(unique_labels))))
        }))

    return dataset_dict


"""
The parsing of the PropBank BR dataset is based on pushdown automata.
The dataset can be found at: http://143.107.183.175:21380/portlex/index.php/pt/projetos/propbankbr
"""


def parser(filepath=FILEPATH):
    dataset_dict = DatasetDict()
    unique_labels = set()

    for split in ["train", "test"]:
        if split == "test":
            filepath = filepath.replace('.conll', '_test.conll')

        with open(os.path.join(filepath), "r", encoding='utf-8') as file:
            dataset = []
            file_str = file.read()
            file_str = file_str.strip()

            document = reset_document()
            stack = []

            for line in tqdm(file_str.split("\n")):
                line = line.strip()

                if line == "":
                    dataset.append(document)
                    document = reset_document()
                    stack = []
                    continue

                tokenized_line = line.split("\t")
                token = tokenized_line[1].strip()
                srl_frames = tokenized_line[9:]

                document["tokens"].append(token)

                # Create N stacks for N verbs
                if len(stack) == 0:
                    for _ in srl_frames:
                        stack.append([])
                        document["srl_frames"].append({
                            "verb": None,
                            "frames": []
                        })

                for i, tag in enumerate(srl_frames):
                    parsed_tag = extract_srl_tags(tag)
                    top_stack = get_top_stack(stack[i])

                    if 'V' == parsed_tag:
                        document["srl_frames"][i]["verb"] = token

                    if '(' in tag:
                        document["srl_frames"][i]['frames'].append(
                            f"B-{parsed_tag}")
                    elif ')' in tag:
                        document["srl_frames"][i]['frames'].append(
                            f"I-{top_stack}")
                    else:

                        if top_stack is not None:
                            document["srl_frames"][i]['frames'].append(
                                f"I-{top_stack}")
                        else:
                            document["srl_frames"][i]['frames'].append("O")

                    if '(' in tag:
                        stack[i].append(parsed_tag)

                    if ')' in tag:
                        stack[i].pop()

                    unique_labels.add(document["srl_frames"][i]['frames'][-1])

        dataset_dict[split] = Dataset.from_list(dataset, split=split)

    return dataset_dict, unique_labels


if __name__ == "__main__":
    dataset_dict, unique_labels = parser()

    for config_name in ['default', 'flatten']:

        if config_name == 'flatten':
            dataset_dict = flatten_dataset(dataset_dict, unique_labels)

        dataset_dict.push_to_hub("liaad/Propbank-BR", config_name=config_name)
