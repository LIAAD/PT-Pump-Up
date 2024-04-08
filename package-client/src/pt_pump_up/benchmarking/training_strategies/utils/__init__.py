def align_labels_with_tokens(tokenized_inputs, labels):

    aligned_labels = []

    for i, label in enumerate(labels):
        # Map tokens to their respective word.
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        type_ids = tokenized_inputs[i].type_ids

        num_special_tokens = len(
            [type_id for type_id in type_ids if type_id != 0])

        if num_special_tokens > 0:
            word_ids = word_ids[:-num_special_tokens]

        previous_word_idx = None

        label_ids = []

        for word_idx in word_ids:  # Set the special tokens to -100.

            if word_idx is None:
                label_ids.append(-100)

            # Only label the first token of a given word.
            elif word_idx != previous_word_idx:
                label_ids.append(label[word_idx])

            else:
                label_ids.append(-100)

            previous_word_idx = word_idx

        aligned_labels.append(label_ids)

    tokenized_inputs['labels'] = labels

    return tokenized_inputs
