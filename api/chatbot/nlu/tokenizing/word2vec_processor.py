from nlu import NLUProcessor
import tensorflow as tf
import numpy as np
import spacy

class Word2VecProcessor(NLUProcessor):
    def __init__(self):
        self.nlp = spacy.load('en_core_web_lg')
    def process(self, data):
        n_sentences = len(data)
        X = np.zeros((n_sentences, self.nlp.vocab.vectors_length))
        for idx, sentence in enumerate(data):
            # Pass each sentence to the nlp object to create a document
            doc = self.nlp(sentence)
            # Save the document's .vector attribute to the corresponding row in     
            # X
            X[idx, :] = doc.vector
        return X
    def process_test(self, data):
        return self.process(data)
