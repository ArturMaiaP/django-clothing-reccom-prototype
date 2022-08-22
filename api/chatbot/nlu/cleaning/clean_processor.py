from nlu import NLUProcessor
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
import regex as re


class CleanProcessor(NLUProcessor):
    def __init__(self, remove_stop_words=False, remove_symbols=False):
        self.encoder = LabelEncoder()
        self.remove_symbols = remove_symbols
        if remove_stop_words:
            self.ignore_words = set(stopwords.words('english'))
        else:
            self.ignore_words = []
    def process(self, data):
        return [self.clean(text) for text in data]

    def process_test(self,data):
        return self.process(data)
    
    def clean(self, text):
        text = text.lower()
        if self.remove_symbols:
            text = re.compile('[/(){}\[\]\|@,;]').sub(' ', text)
            text = re.compile('[^0-9a-z #+_]').sub(' ', text)
        else:
            text = re.compile('([/(){}\[\]\|@,;])').sub(' \\1 ', text)
            text = re.compile('([^0-9a-z #+_])').sub(' \\1 ', text)
            while "  " in text:
                text = text.replace("  ", " ")
        return ' '.join(word for word in text.split() if word not in self.ignore_words)
