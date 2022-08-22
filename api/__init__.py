from flask import Flask, request, jsonify
from api.models.user import User
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
import jwt
import pandas as pd

from .recommender.SelectImages import SelectImages
from .chatbot import Chatbot

from dotenv import load_dotenv
load_dotenv('.env')

login_manager = LoginManager()
login_manager.session_protection = "strong"

chatbotInstance = Chatbot()
bcrypt = Bcrypt()
select_images = SelectImages()
cors = CORS()

def login_required(f):
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({'message': "Unathorized"}), 401
        try:
            data = jwt.decode(token.split(" ")[1], os.getenv('SECRET_KEY'), algorithms=['HS256'])
            user = User.query.filter_by(id=data['sub']).first()
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
    cors.init_app(app)
    
    from .models import db, Product
    db.init_app(app)
    
    with app.app_context():
        select_images.init_app(pd.read_sql(Product.query.statement, db.engine)[["name", "x", "y"]])

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .recommend import recommend as recommend_blueprint
    app.register_blueprint(recommend_blueprint)
    
    from .product import product as product_blueprint
    app.register_blueprint(product_blueprint)
    
    from .chat import chatbot_blueprint
    app.register_blueprint(chatbot_blueprint)

    return app