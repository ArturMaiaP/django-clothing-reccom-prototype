from math import e, log
import numpy as np
class EntropyCalculator:
    def __init__(self) -> None:
        #self.nlp = spacy.load('en_core_web_sm')
        self.entities = [
            #Label, Patterns
            ["pattern", [
                ["a_line", "a[\ -]+line"],
                ["dots", "dot(s|ted)?"],
                ["Floral", "flo(ral|wer)"],
                ["Printed", "print(ed)?"],
                ["Stripes", "stripe(s|d)?"],
            ]],
            ["fabric", [
                ["denim", "denim"],
                ["faux", "faux(?! leather)"],
                ["faux_leather", "faux[\ -]+leather"],
                ["knit", "knit(ted)?"],
                ["Lacy", "lac(e|y|ed)"],
                ["leather", "(?<!faux )leather"],
            ]],
            ["size", [
                ["maxi", "(long(er)?)"],
                ["midi", "(mid)"],
                ["mini", "(mini)"],
            ]],
            ["format", [
                ["pencil", "pencil"],
                ["Pleated", "pleat(ed)?"],
                ["skater", "skater"],
            ]],
        ]
    def entropy(self, df):       
        l = {}
        for label, ent in self.entities:
            n = len(df)
            if n <= 1:
                l[label] = 0.
                continue
            probs = []
            for key, pattern in ent:
                probs.append(len(df[df[key] == 1]) / n)
                
            if np.count_nonzero(probs) <= 1:
                l[label] = 0.
                continue
            
            ent = 0.
            for i in probs:
                if i > 0:
                    ent -= i * log(i, e)
            l[label] = ent
        return l
                    