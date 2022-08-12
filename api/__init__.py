from flask import Flask, request, jsonify
from api.models.user import get_user_by_id
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flaskext.mysql import MySQL
import os
import jwt
from pymysql.cursors import DictCursor

from dotenv import load_dotenv
load_dotenv('.env')

login_manager = LoginManager()
login_manager.session_protection = "strong"

bcrypt = Bcrypt()
mysql = MySQL(cursorclass=DictCursor)

def login_required(f):
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({'message': "Unathorized"}), 401
        try:
            data = jwt.decode(token.split(" ")[1], os.getenv('SECRET_KEY'), algorithms=['HS256'])
            user = get_user_by_id(mysql.get_db(), data['sub'])
            if not user:
                return jsonify({'message': "Unathorized"}), 401
        except Exception as e:
            print(e)
            return jsonify({'message': "Unathorized"}), 401
        return f(user, *args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated

def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('config.py')
    
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mysql.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .recommend import recommend as recommend_blueprint
    app.register_blueprint(recommend_blueprint)

    return app