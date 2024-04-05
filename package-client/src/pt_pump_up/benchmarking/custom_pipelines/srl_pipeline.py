from transformers import Pipeline 
import numpy as np


class SRLPipeline(Pipeline):

    def align_labels_with_tokens(self, word_ids, type_ids=None):

        if type_ids is not None:
            # Obtain the number of type_ids different from 0
            num_special_tokens = len(
                [type_id for type_id in type_ids if type_id != 0])
            # Remove the special tokens from the word_ids
            word_ids = word_ids[:-num_special_tokens]

        previous_word_idx = None
        label_ids = []

        for word_idx in word_ids:  # Set the special tokens to -100.
            if word_idx is None:
                label_ids.append(-100)
            # Only label the first token of a given word.
            elif word_idx != previous_word_idx:
                label_ids.append(0)
            else:
                label_ids.append(-100)

            previous_word_idx = word_idx

        return label_ids

    def _sanitize_parameters(self, **kwargs):
        preprocess_kwargs = {}

        if "verb" in kwargs:
            preprocess_kwargs["verb"] = kwargs["verb"]

        return preprocess_kwargs, {}, {}

    def preprocess(self, text, verb=None):
        print(f"Text: {text}, Verb: {verb}")

        tokenized_results = self.tokenizer(text, verb, truncation=True,
                                           max_length=self.model.config.max_position_embeddings,
                                           return_tensors=self.framework)

        self.labels = self.align_labels_with_tokens(
            tokenized_results.word_ids(0), tokenized_results[0].type_ids)

        self.label_names = self.model.config.id2label

        return tokenized_results

    def _forward(self, model_inputs):
        return self.model(**model_inputs)

    def postprocess(self, model_outputs):
        logits = model_outputs.logits

        predictions = np.argmax(logits, axis=-1).squeeze().tolist()

        true_predictions = []

        for prediction, label in zip(predictions, self.labels):
            if label != -100:
                true_predictions.append(self.label_names[prediction])

        return true_predictions