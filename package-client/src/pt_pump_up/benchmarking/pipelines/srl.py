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

    def align_labels_with_tokens(self, tokenized_inputs, all_labels):
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
                else:
                    new_labels.append(-100)

            results.append(new_labels)

        tokenized_inputs['labels'] = results

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
                tokenized_inputs=tokenized_results, all_labels=[raw_labels])

            self.labels = tokenized_results["labels"]

            # Remove labels temporarily to avoid conflicts in the forward pass
            tokenized_results.pop("labels")

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

            doc = self.nlp(self.text.strip())

            outputs.append({
                "tokens": [token.text for token in doc],
                "predictions": true_predictions,
                "verb": self.verbs[i]
            })

        return outputs
