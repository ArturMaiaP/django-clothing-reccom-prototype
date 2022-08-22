from nlu import NLUProcessor
from sklearn.preprocessing import LabelEncoder


class LabelProcessor(NLUProcessor):
    def __init__(self):
        self.encoder = LabelEncoder()
    def process(self, data):
        return self.encoder.fit_transform(data)
    def process_test(self, data):
        return self.encoder.transform(data)