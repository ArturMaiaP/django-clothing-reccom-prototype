from flask import Blueprint, request, jsonify

from .models.user import User

from .models import db
from . import bcrypt
import datetime
import jwt
import os
import uuid

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    uid = request.json.get('uid')

    try:
        user = User.query.filter_by(uid=uid).first()
        token = jwt.encode({
            "sub": user.id,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=8)
        }, os.getenv('SECRET_KEY'))
        return jsonify({"user": {
            "token": token,
            "uid": user.uid
        }})
    except Exception as e:
        print("[Error] Login")
        print(e)
    return jsonify({"message": "Some error."}), 500


@auth.route('/signup', methods=['POST'])
def signup():
    uid = str(uuid.uuid4())

    try:
        user = User(uid=uid)
        db.session.add(user)
        db.session.commit()
        token = jwt.encode({
            "sub": user.id,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=8)
        }, os.getenv('SECRET_KEY'))
        return jsonify({"user": {
            "token": token,
            "uid": user.uid
        }})
    except Exception as e:
        print("[Error] Signup")
        print(e)
    return jsonify({"message": "Some error."}), 500
