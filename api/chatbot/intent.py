from .model.data import Data
import pickle
import os

class IntentClassifier:
    def __init__(self):
        self.data = Data.load(os.path.join(os.path.dirname(__file__), "model/data.pkl"))
        self.model = pickle.load(open(os.path.join(os.path.dirname(__file__), "model/model.h5"), "rb"))
    def predict(self, text):
        return self.model.predict_proba(self.data.get_bow([text])).tolist()[0]