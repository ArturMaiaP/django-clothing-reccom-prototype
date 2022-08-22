from .model.data import Data
import pickle
import os

class IntentClassifier:
    def __init__(self):
        self.data = Data.load('./api/chatbot/model/data.pkl')
        self.model = pickle.load(open("./api/chatbot/model/model.h5", "rb"))
    def predict(self, text):
        return self.model.predict_proba(self.data.get_bow([text])).tolist()[0]