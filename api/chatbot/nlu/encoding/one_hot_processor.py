from nlu import NLUProcessor
from util import binary_search
import numpy as np
from sklearn.preprocessing import OneHotEncoder

class OneHotProcessor(NLUProcessor):
    def __init__(self):
        self.encoder = OneHotEncoder()
    def process(self, data):
        self.classes = sorted(set(data))
        empty_arr = [0] * len(self.classes)

        bags = []
        for w in data:
            bag = list(empty_arr)
            bag[binary_search(self.classes, w)] = 1
            bags.append(bag)
        return bags
    def process_test(self, data):
        empty_arr = [0] * len(self.classes)

        bags = []
        for w in data:
            bag = list(empty_arr)
            bag[binary_search(self.classes, w)] = 1
            bags.append(bag)
        return bags