from .DialogPolicy import DialogPolicy
from .entity import EntityExtractor
from .intent import IntentClassifier

class Chatbot:
    def __init__(self) -> None:
        self.intent_classifier = IntentClassifier()
        self.dialog_policy = DialogPolicy()
        self.entity_extractor = EntityExtractor()
    def intent(self, text):
        return self.intent_classifier.predict(text)
    def entities(self, text):
        return self.entity_extractor.extract(text)
    def do(self, data):
        if data['action'] == 'answer':
            return data['text']
        elif data['action'] == 'recommend':
            return "recommend"
    def turn(self, state, text):
        intent = self.intent(text)
        entities = self.entities(text)
        data = self.dialog_policy.answer(state, text, intent, entities)
        return data
    
    def get_state(self):
        return self.state