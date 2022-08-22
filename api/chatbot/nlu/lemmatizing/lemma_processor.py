from nlu import NLUProcessor
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet

class LemmaProcessor(NLUProcessor):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
    def process(self, data):
        return [' '.join([self.lemmatizer.lemmatize(word.lower(), self.get_wordnet_pos(word.lower())) for word in word_tokenize(doc)]) for doc in data]
    def process_test(self,data):
        return self.process(data)
    def get_wordnet_pos(self, word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)