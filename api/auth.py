from flask import Blueprint, request, jsonify

from .models.user import User

from .models import db
from . import bcrypt
import datetime
import jwt
import os

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    
    try:
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            token = jwt.encode({
                "sub": user.id,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=4)
            }, os.getenv('SECRET_KEY'))
            return jsonify({"token": token})
        else:
            return jsonify({"message": "Email or password is invalid."}), 422
    except Exception as e:
        print("[Error] Login")
        print(e)
    return jsonify({"message": "Some error."}), 500

@auth.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')
    name = request.json.get('name')
    
    try:
        user = User(name=name, email=email, password=bcrypt.generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "OK"})
    except Exception as e:
        print("[Error] Signup")
        print(e)
    return jsonify({"message": "Some error."}), 500
