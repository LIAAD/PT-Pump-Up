import spacy
import numpy as np
from transformers import Pipeline


class SRLPipeline(Pipeline):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        spacy.prefer_gpu()

        if not spacy.util.is_package("pt_core_news_sm"):
            spacy.cli.download("pt_core_news_sm")

        self.nlp = spacy.load("pt_core_news_sm")

    def align_labels_with_tokens(self, tokenized_inputs, labels):

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

        self.labels = labels

        return tokenized_inputs

    def _sanitize_parameters(self, **kwargs):
        preprocess_kwargs = {}

        if "verb" in kwargs:
            preprocess_kwargs["verb"] = kwargs["verb"]

        return preprocess_kwargs, {}, {}

    def preprocess(self, text):

        self.text = text

        doc = self.nlp(text.strip())

        self.label_names = self.model.config.id2label

        # Extract list with verbs from the text
        self.verbs = [token.text for token in doc if token.pos_ == "VERB"]

        results = []

        tokenized_input = [token.text for token in doc]
        raw_labels = [0] * len(tokenized_input)

        for verb in self.verbs:
            tokenized_results = self.tokenizer(
                tokenized_input, [verb], truncation=True,
                is_split_into_words=True,
                return_tensors="pt", max_length=self.model.config.max_position_embeddings)

            tokenized_results = self.align_labels_with_tokens(
                tokenized_inputs=tokenized_results, labels=[raw_labels])

            results.append(tokenized_results)

        return results

    def _forward(self, batch_inputs):
        results = []

        for entry in batch_inputs:
            results.append(self.model(**entry))

        return results

    def postprocess(self, batch_outputs):
        outputs = []

        for i, entry in enumerate(batch_outputs):
            logits = entry.logits

            predictions = np.argmax(logits, axis=-1).squeeze().tolist()

            true_predictions = []

            for prediction, label in zip(predictions, self.labels[0]):
                if label != -100:
                    true_predictions.append(self.label_names[prediction])

            outputs.append({
                "tokens": self.text.split(),
                "predictions": true_predictions,
                "verb": self.verbs[i]
            })

        return outputs
