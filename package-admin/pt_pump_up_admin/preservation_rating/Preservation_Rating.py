import pandas as pd
from abc import ABC, abstractmethod
from sklearn import tree
import huggingface_hub
import logging
import pickle
import requests
import os
import numpy as np
from datetime import datetime
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder


class PreservationRating(ABC):
    @abstractmethod
    def __init__(self, url_fetch, local_path, hf_token, hf_repo, hf_path, use_cache) -> None:
        if hf_token is None:
            raise ValueError("HuggingFace token is required")

        self.hf_token = hf_token
        self.hf_path = hf_path
        self.clf = None
        self.local_path = local_path
        self.url_fetch = url_fetch
        self.hf_repo = hf_repo

        try:
            if use_cache:
                logging.info("Loading model from HuggingFace Hub")

                path = huggingface_hub.hf_hub_download(
                    repo_id=hf_repo,
                    filename=hf_path,
                    token=hf_token,
                )

                logging.info(f"Loading model from {path}")

                with open(path, "rb") as f:
                    self.clf = pickle.load(f)

                logging.info(
                    f"Model loaded successfully | Type: {type(self.clf)}")

        except Exception as e:
            logging.error("Error loading model from HuggingFace Hub")
            logging.error(e)

    def fetch_all(self):
        response = requests.get(self.url_fetch)

        if response.status_code == 200:
            return pd.DataFrame(data=response.json())
        else:
            raise ValueError("Error fetching datasets")

    @abstractmethod
    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    def root_train(self, **params):
        df = self.fetch_all()

        X, y = self.preprocess(df)

        self.clf = tree.DecisionTreeClassifier(**params)

        self.clf.fit(X=X, y=y)

        self.save_model()

    def active_train(self, df: pd.DataFrame):
        X, y = self.preprocess(df)

        self.clf.fit(X=X, y=y)

        self.save_model()

    def predict(self, series: pd.Series) -> str:
        df = pd.DataFrame(data=[series])

        X, _, encoder = self.preprocess(df)

        output = self.clf.predict(X=X)

        return encoder.inverse_transform(output.reshape(-1, 1)).item()

    def save_model(self):
        if self.clf is None:
            raise ValueError("No model to save")

        with open(self.local_path, "wb") as f:
            pickle.dump(self.clf, f)

        huggingface_hub.HfApi().upload_file(
            path_or_fileobj=self.local_path,
            path_in_repo=self.hf_path,
            repo_id=self.hf_repo,
            token=self.hf_token,
            commit_message="Rating model update"
        )


class PreservationRatingDataset(PreservationRating):

    def __init__(self, hf_token, hf_repo, hf_path=None, use_cache=False) -> None:
        super().__init__(url_fetch="http://pt-pump-up.inesctec.pt/api/datasets",
                         local_path=os.path.join(
                             os.getcwd(), "out", "dataset_model.pkl"),
                         hf_token=hf_token, hf_repo=hf_repo, hf_path=hf_path, use_cache=use_cache)

    def preprocess(self, df: pd.DataFrame):
        df = pd.concat([df.drop(['hrefs', 'status'], axis=1), df['hrefs'].apply(
            pd.Series), df['status'].apply(pd.Series)], axis=1)

        df.drop(columns=['id', 'english_name', 'full_portuguese_name', 'description', 'language_stats',
                'conference', 'overall_dataset_stats', 'authors', 'license', 'nlp_tasks', 'doi'], inplace=True)

        df['introduction_date'] = df['introduction_date'].apply(
            lambda x: int(datetime.strptime(x, '%Y/%m/%d').timestamp()))

        # TODO: Discard This Hack
        df['link_source'] = df['link_source'].fillna(
            'https://www.nowebsite.com')

        df['link_source'] = df['link_source'].apply(
            lambda x: x if x.startswith('http') else 'https://www.nowebsite.com' + x)

        df['link_source'] = df['link_source'].str.extract(
            r'^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)')

        df['link_source'] = df['link_source'].apply(lambda x: x.split('.')[1])

        df['link_hf'] = df['link_hf'].fillna('nolink')

        # Cast Columns
        df['introduction_date'] = df['introduction_date'].astype('int64')
        df['link_source'] = df['link_source'].astype('category')
        df['link_hf'] = df['link_hf'].astype('category')
        df['broken_link'] = df['broken_link'].astype('bool')
        df['author_response'] = df['author_response'].astype('bool')
        df['standard_format'] = df['standard_format'].astype('bool')
        df['backup'] = df['backup'].astype('bool')
        df['preservation_rating'] = df['preservation_rating'].astype(
            'category')
        df['off_the_shelf'] = df['off_the_shelf'].astype('bool')

        for column in ['link_source', 'link_hf']:
            label_encoder = LabelEncoder()
            df[column] = label_encoder.fit_transform(df[column])

        ordinal_encoder = OrdinalEncoder(dtype=np.int64, categories=[
                                         ['low', 'medium', 'high']])

        df['preservation_rating'] = ordinal_encoder.fit_transform(
            df[['preservation_rating']])

        # Split in X and y
        X = df.drop(columns=['preservation_rating']).to_numpy()
        y = df['preservation_rating'].to_numpy()

        return X, y, ordinal_encoder


class PreservationRatingModel(PreservationRating):

    def __init__(self, hf_token, hf_repo, hf_path=None, use_cache=False) -> None:
        super().__init__(url_fetch="http://pt-pump-up.inesctec.pt/api/models",
                         local_path=os.path.join(
                             os.getcwd(), "out", "model_model.pkl"),
                         hf_token=hf_token, hf_repo=hf_repo, hf_path=hf_path, use_cache=use_cache),

    def preprocess(self, df: pd.DataFrame):
        raise NotImplementedError()
