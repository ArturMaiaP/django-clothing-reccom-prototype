import spacy
import re
from spacy import displacy
from collections import Counter

class EntityExtractor:
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
    def extract(self, text):
        ents = []
        for label, ent in self.entities:
            for key, pattern in ent:
                x = re.search(pattern, text.lower())
                if x:
                    ents.append([key , label])
        return ents