import time
import numpy as np
import random

class DialogPolicy:
    def __init__(self):
        self.answers = [
            #ASK:GET
            ["ANSWER to ASK:GET"],
            #INFORM:DISAMBIGUATE
            ["Which do you mean?", "Which one?", "Which one exactly?", "Which one again?"],
            #INFORM:GET
            ["ANSWER to INFORM:GET"],
            #INFORM:REFINE
            ["ANSWER to INFORM:REFINE"],
            #REQUEST:ADD_TO_CART
            ["Of course. I'll add now.", "Yes, I'll update your cart for you.", "Nice choice, I'll add them to your cart."],
            #REQUEST:COMPARE
            ["ANSWER to REQUEST:COMPARE"],
            #REQUEST:GET
            ["ANSWER to REQUEST:GET"]
        ]
        self.slots = [
            #ASK:GET
            ["type", "color", "pattern"],
            #INFORM:DISAMBIGUATE
            ["type", "color", "pattern"],
            #INFORM:GET
            ["type", "color", "pattern"],
            #INFORM:REFINE
            ["type", "color", "pattern"],
            #REQUEST:ADD_TO_CART
            ["item"],
            #REQUEST:COMPARE
            ["item", "with_item"],
            #REQUEST:GET
            ["type", "color", "pattern"]
        ]
        
    def response(self, i):
        return random.choice(self.answers[i])
    
    def recommend_text(self):
        return random.choice(["Perhaps you'd like this one?", "What do you think about this one?"])
    
    def process_slots(self,state, i,entities):
        for slot in self.slots[i]:
            if slot not in state['slots']:
                state['slots'][slot] = []
        
        #Fill slots                
        for ent in entities:
            if ent.label_ in state['slots']:
                state['slots'][ent.label_].append(ent.text)
    
    def answer(self, state, text, intent, entities):
        intent_index = np.argmax(intent)
        now = time.time()
        elapsed = now - state['turns'][-1]['time'] if len(state['turns']) else 0
        state['turns'].append({'time': now, 'text': text, 'entities': entities})
        
        self.process_slots(state, intent_index, entities)
        
        resp = [{"action": "answer", "text": self.response(intent_index)}]
        if elapsed >= 30:
            resp.append({"action": "recommend", "text": self.recommend_text()})
        return resp