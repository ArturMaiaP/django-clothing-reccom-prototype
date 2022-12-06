from flask import Blueprint, jsonify, request
import json

from . import login_required, chatbotInstance, select_images
from .models import db, Chat, Logs
from .chatbot import Chatbot

chatbot_blueprint = Blueprint('chatbot', __name__)

@chatbot_blueprint.route('/chat', methods=['POST'])
@login_required
def chat(user):
    id = request.json.get('id')
    text = request.json.get('text')
    
    session = Chat.query.filter_by(id=id, user_id=user.id).first()
    if session:
        state = json.loads(session.session)
        state['entropy'] = select_images.entropy(state['slots'])
        actions = chatbotInstance.turn(state, text)
        session.session = json.dumps(state)
        db.session.add(session)
        db.session.commit()
        
        logs = Logs()
        logs.description = json.dumps({"action": '/chat', "user": user, "data": {"chat": id, "input": text, "result": actions}})
        db.session.add(logs)
        db.session.commit()
        return jsonify({"actions": actions})
    return jsonify({"message": "Session invalid."}), 422

@chatbot_blueprint.route('/chat/init', methods=['POST'])
@login_required
def chat_init(user):
    state = {
        "turns": [],
        "slots": {}
    }
    chat = Chat(user_id = user.id, session = json.dumps(state))
    db.session.add(chat)
    db.session.commit()
        
    logs = Logs()
    logs.description = json.dumps({"action": '/chat/init', "user": user, "data": {"chat": chat.id}})
    db.session.add(logs)
    db.session.commit()
    return jsonify({"id": chat.id})
