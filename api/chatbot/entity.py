import spacy
from spacy import displacy
from collections import Counter

class EntityExtractor:
    def __init__(self) -> None:
        self.nlp = spacy.load('en_core_web_sm')
    def extract(self, text):
        doc = self.nlp(text)
        return doc.ents