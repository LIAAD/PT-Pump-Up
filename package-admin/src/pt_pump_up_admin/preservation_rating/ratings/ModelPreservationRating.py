from numpy.core.multiarray import array as array
from pandas import DataFrame
from pt_pump_up_admin.preservation_rating import PreservationRating
import numpy as np

class ModelPreservationRating(PreservationRating):
    def __init__(self, hf_repo, hf_path, hf_token):
        super().__init_(hf_repo, hf_path, hf_token)

    def preprocess(self, data: DataFrame) -> tuple:
        raise NotImplementedError

    def postprocess(self, X: np.array) -> np.array:
        raise NotImplementedError
