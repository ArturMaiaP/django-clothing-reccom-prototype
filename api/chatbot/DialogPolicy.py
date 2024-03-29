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
            ["size", "format", "fabric", "pattern"],
            #INFORM:DISAMBIGUATE
            ["size", "format", "fabric", "pattern"],
            #INFORM:GET
            ["size", "format", "fabric", "pattern"],
            #INFORM:REFINE
            ["size", "format", "fabric", "pattern"],
            #REQUEST:ADD_TO_CART
            ["item"],
            #REQUEST:COMPARE
            ["item", "with_item"],
            #REQUEST:GET
            ["size", "format", "fabric", "pattern"]
        ]
        
    def response(self, i, elapsed):
        responses = []
        shouldRecommend = False

        if i in [1,4]:
            responses.append({"action": "answer", "text": random.choice(self.answers[i])})
        else:
            shouldRecommend = True
        
        if elapsed >= 30 or shouldRecommend:
            responses.append({"action": "recommend", "text": self.recommend_text()})
        
        return responses
    
    def recommend_text(self):
        return random.choice(["Perhaps you'd like one of these?", "What do you think about one of these?"])
    
    def process_slots(self,state, i,entities):
        for slot in self.slots[i]:
            if slot not in state['slots']:
                state['slots'][slot] = []
        
        #Fill slots                
        for ent in entities:
            if ent[1] in state['slots'] and ent[0] not in state['slots'][ent[1]]:
                state['slots'][ent[1]].append(ent[0])
    
    def answer(self, state, text, intent, entities):
        intent_index = np.argmax(intent)
        now = time.time()
        elapsed = now - state['turns'][-1]['time'] if len(state['turns']) else 0
        state['turns'].append({'time': now, 'text': text, 'entities': entities})
        
        self.process_slots(state, intent_index, entities)
        
        return self.response(intent_index, elapsed)