
# Adapted from: https://huggingface.co/learn/nlp-course/chapter7/2?fw=pt

def align_labels_with_tokens(tokenized_inputs, all_labels):
    results = []

    for i, labels in enumerate(all_labels):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        type_ids = tokenized_inputs[i].type_ids

        num_special_tokens = len(
            [type_id for type_id in type_ids if type_id != 0])

        if num_special_tokens > 0:
            word_ids = word_ids[:-num_special_tokens]

        new_labels = []
        current_word = None

        for word_id in word_ids:
            if word_id != current_word:
                # Start of a new word!
                current_word = word_id
                label = -100 if word_id is None else labels[word_id]
                new_labels.append(label)
            elif word_id is None:
                # Special token
                new_labels.append(-100)
            else:

                new_labels.append(-100)

        results.append(new_labels)

    tokenized_inputs['labels'] = results

    return tokenized_inputs

# Adapted from: https://huggingface.co/docs/transformers/tasks/question_answering


def post_process_training_question_answering(tokenized_inputs, answers):
    start_positions = []
    end_positions = []

    offset_mapping = tokenized_inputs.pop("offset_mapping")

    for i, offset in enumerate(offset_mapping):
        answer = answers[i]
        start_char = answer["answer_start"][0]
        end_char = answer["answer_start"][0] + len(answer["text"][0])
        sequence_ids = tokenized_inputs.sequence_ids(i)

        # Find the start and end of the context
        idx = 0
        while sequence_ids[idx] != 1:
            idx += 1
        context_start = idx
        while sequence_ids[idx] == 1:
            idx += 1
        context_end = idx - 1

        # If the answer is not fully inside the context, label it (0, 0)
        if offset[context_start][0] > end_char or offset[context_end][1] < start_char:
            start_positions.append(0)
            end_positions.append(0)
        else:
            # Otherwise it's the start and end token positions
            idx = context_start
            while idx <= context_end and offset[idx][0] <= start_char:
                idx += 1
            start_positions.append(idx - 1)

            idx = context_end
            while idx >= context_start and offset[idx][1] >= end_char:
                idx -= 1
            end_positions.append(idx + 1)

    return start_positions, end_positions


def post_process_validation_question_answering(tokenized_inputs, raw_ids):
    sample_map = tokenized_inputs.pop("overflow_to_sample_mapping")
    example_ids = []

    for i in range(len(tokenized_inputs["input_ids"])):
        sample_idx = sample_map[i]
        example_ids.append(raw_ids[sample_idx])

        sequence_ids = tokenized_inputs.sequence_ids(i)
        offset = tokenized_inputs["offset_mapping"][i]
        tokenized_inputs["offset_mapping"][i] = [
            o if sequence_ids[k] == 1 else None for k, o in enumerate(offset)
        ]

    tokenized_inputs["example_id"] = example_ids
