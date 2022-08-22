import json
import pickle
from sklearn.model_selection import train_test_split
import numpy as np
import os
import sys

class Data:
    def __init__(self, file, x_processors=[], y_processors=[], test_data=None):
        self.X = []
        self.Y = []
        self.X_test = []
        self.Y_test = []
        self.x_processors = x_processors
        self.y_processors = y_processors
        self.words = []
        self.classes = []
        self.rev_classes = {}
        if test_data:
            self.load_test_data(test_data)
        self.load_data(file)
        self.process_data()
        for i in self.classes:
            self.rev_classes[self.get_class([i])[0]] = i

    def load_data(self, file):
        data_file = open(file)
        data = json.loads(data_file.read())['intents']
        data_file.close()

        for intent in data:
            for pattern in intent['patterns']:
                self.words.extend(pattern)
                self.X.append(pattern)
                self.Y.append(intent['tag'])
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        self.words = sorted(list(set(self.words)))
        self.classes = sorted(list(set(self.classes)))

    def load_test_data(self, file):
        data_file = open(file)
        data = json.loads(data_file.read())['intents']
        data_file.close()

        for intent in data:
            for pattern in intent['patterns']:
                self.words.extend(pattern)
                self.X_test.append(pattern)
                self.Y_test.append(intent['tag'])
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        self.words = sorted(list(set(self.words)))
        self.classes = sorted(list(set(self.classes)))

    def process_data(self):
        for p in self.x_processors:
            self.X = p.process(self.X)

        for p in self.y_processors:
            self.Y = p.process(self.Y)

        if len(self.X_test) > 0:
            for p in self.x_processors:
                self.X_test = p.process_test(self.X_test)
            for p in self.y_processors:
                self.Y_test = p.process_test(self.Y_test)

    def get_trainnig_data(self, validation=True):
        if len(self.X_test) > 0:
            x_train = np.array(self.X)
            x_test = np.array(self.X_test)
            y_train = np.array(self.Y)
            y_test = np.array(self.Y_test)
        else:
            x_train, x_test, y_train, y_test=train_test_split(np.array(self.X), np.array(
                self.Y), stratify = self.Y, test_size = 0.3, shuffle = True)
        if validation:
            x_train, x_val, y_train, y_val=train_test_split(
                x_train, y_train, stratify = y_train, test_size = 0.3, shuffle = True)
            return (x_train, x_val, x_test, y_train, y_val, y_test)

        return (x_train, x_test, y_train, y_test)

    def get_bow(self, sentence):
        for p in self.x_processors:
            sentence=p.process_test(sentence)

        return sentence

    def get_class(self, tag):
        for p in self.y_processors:
            tag=p.process_test(tag)

        return tag

    def dump(self, path):
        pickle.dump(self, open(path, 'wb'))

    @ classmethod
    def load(cls, path):
        sys.path.append(os.path.join(os.getcwd(), "./api/chatbot"))
        return pickle.load(open(path, 'rb'))

    def __str__(self):
        s="words: "+str(self.words)+"\n"
        s += "classes: "+str(self.classes)+"\n"
        return s
    def __getstate__(self):
        return (self.classes, self.x_processors, self.y_processors)
    def __setstate__(self,state):
        self.classes, self.x_processors, self.y_processors = state
