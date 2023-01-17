from math import e, log
import numpy as np
class EntropyCalculator:
    def __init__(self) -> None:
        #self.nlp = spacy.load('en_core_web_sm')
        self.entities = [
            #Label, Patterns
            ["color", [
               ["black", "black"],
               ["blue", "blue"],
               ["brown", "brown"],
               ["beige", "beige"],
               ["gray", "gr(a|e)y"],
               ["green", "green"],
               ["orange", "orange"],
               ["pink", "pink"],
               ["purple", "purple"],
               ["red", "(red)"],
               ["white", "white"],
               ["yellow", "yellow"],
            ]],
            ["fabric", [
                ["denim", "(denim|jean(s)?)"],
                ["knitted", "(knit(ted)?|whool)"],
                ["laced", "(lac(e|y|ed)|jacquard)"],
                ["glossy", "(leather|glossy)"],
                ["velvet", "(velvet|plushy)"],
                ["general", "(cotton|jersey|silk|satin)"],
            ]],
            ["pattern", [
                ["animal_print", "animal([\ -]+print)?"],
                ["geometric", "(geometric|argyle)"],
                ["camouflage", "camouflage"],
                ["checked", "(checked|plaid)"],
                ["floral", "flo(ral|wer)"],
                ["paisley", "paisley"],
                ["plain", "plain"],
                ["dots", "dot(s|ted)?"],
                ["striped", "stripe(s|d)?"],
                ["tie_dyed", "tie[\ -]+dye(d)?"],
            ]],
            ["size", [
                ["maxi", "(max(i)?|long(er)?)"],
                ["midi", "(mid(i)?)"],
                ["mini", "(mini|short)"],
            ]],
            ["type", [
                ["straight", "(pencil|straight|bubble|tulip)"],
                ["pleated", "((pleat(s|es|ed)?)|a[\ -]+line|yoke|panel|tiered|gathered|godet)"],
                ["skewed", "(skewed|wrap|hankerchief|sarong|assymetric)"],
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
                probs.append(len(df[df[label] == key]) / n)
                
            if np.count_nonzero(probs) <= 1:
                l[label] = 0.
                continue
            
            ent = 0.
            for i in probs:
                if i > 0:
                    ent -= i * log(i, e)
            l[label] = ent
        return l
                    