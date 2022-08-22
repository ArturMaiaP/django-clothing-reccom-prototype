from nlu import NLUProcessor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder


class TfidfProcessor(NLUProcessor):
    def __init__(self):
        self.encoder = TfidfVectorizer()
    def process(self, data):
        return self.encoder.fit_transform(data).toarray()
    def process_test(self, data):
        return self.encoder.transform(data).toarray()