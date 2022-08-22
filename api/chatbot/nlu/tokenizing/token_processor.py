from nlu import NLUProcessor
import tensorflow as tf

import nltk

class TokenProcessor(NLUProcessor):
    def __init__(self, num_words=50000, max_len=100):
        self.tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=num_words, filters="")
        self.max_len=max_len
    def process(self, data):
        self.tokenizer.fit_on_texts(data)
        self.word_index = self.tokenizer.word_index
        sequences = self.tokenizer.texts_to_sequences(data)
        return tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=self.max_len)
    def process_test(self, data):
        sequences = self.tokenizer.texts_to_sequences(data)
        return tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=self.max_len)
