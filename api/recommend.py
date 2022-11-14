from flask import Blueprint, jsonify, request
import json

from . import login_required, select_images
from .models import db, Preference, Product, Chat, Finish
from .recommender.Constantes import *

recommend = Blueprint('recommend', __name__)

@recommend.route('/finish', methods=['POST'])
@login_required
def finish(user):
    product = Product.query.filter_by(name=request.json.get('product')).first()
    if product:
        finished = Finish.query.filter_by(user_id = user.id).first()
        if not finished:
            finished = Finish(user_id = user.id, product_id = product.id)
        finished.product_id = product.id
        db.session.add(finished)
        db.session.commit()
        return jsonify({"message": "OK"})
    return jsonify({"message": "Product invalid."}), 422

@recommend.route('/like', methods=['POST'])
@login_required
def like(user):
    product = Product.query.filter_by(name=request.json.get('product')).first()
    if product:
        pref = Preference.query.filter_by(user_id = user.id, product_id = product.id).first()
        if not pref:
            pref = Preference(user_id = user.id, product_id = product.id)
        pref.liked = True
        db.session.add(pref)
        db.session.commit()
        return jsonify({"message": "OK"})
    return jsonify({"message": "Product invalid."}), 422

@recommend.route('/dislike', methods=['POST'])
@login_required
def dislike(user):
    product = Product.query.filter_by(name=request.json.get('product')).first()
    if product:
        pref = Preference.query.filter_by(user_id = user.id, product_id = product.id).first()
        if not pref:
            pref = Preference(user_id = user.id, product_id = product.id)
        pref.liked = False
        db.session.add(pref)
        db.session.commit()
        return jsonify({"message": "OK"})
    return jsonify({"message": "Product invalid."}), 422

@recommend.route('/recommend', methods=['GET'])
@login_required
def recomm(user):
    liked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=user.id, liked=1).all()]
    disliked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=user.id, liked=0).all()]

    id = request.args.get('id')
    slots = None
    if id:
        session = Chat.query.filter_by(id=id, user_id=user.id).first()
        if session:
            state = json.loads(session.session)
            slots = state['slots']
    
    if (len(liked) < TAMANHO_MINIMO_SVM) or (len(disliked) < TAMANHO_MINIMO_SVM):
        list_img_ini = select_images.select_images_distance(slots)
    else:
        list_img_ini = select_images.select_images_svm(liked, disliked, slots)
    
    return jsonify({'img_list': list_img_ini})

@recommend.route('/recommend/best', methods=['GET'])
@login_required
def best(user):
    liked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=1, liked=1).all()]
    disliked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=1, liked=0).all()]
    
    id = request.args.get('id')
    slots = None
    if id:
        session = Chat.query.filter_by(id=id, user_id=user.id).first()
        if session:
            state = json.loads(session.session)
            slots = state['slots']
            
    jsonify({'img': select_images.select_best_svm(liked, disliked, slots)})
    
    