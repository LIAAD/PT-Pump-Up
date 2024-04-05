
def align_labels_with_tokens(labels, word_ids, type_ids=None):

    if type_ids is not None:
        # Obtain the number of type_ids different from 0
        num_special_tokens = len(
            [type_id for type_id in type_ids if type_id != 0])
        # Remove the special tokens from the word_ids
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
            # Same word as previous token
            label = labels[word_id]
            # If the label is B-XXX we change it to I-XXX
            if label % 2 == 1:
                label += 1
            new_labels.append(label)

    return new_labels
