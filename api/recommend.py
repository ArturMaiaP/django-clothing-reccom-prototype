from flask import Blueprint, jsonify, request

from . import login_required, select_images
from .models import db, Preference, Product
from .recommender.Constantes import *

recommend = Blueprint('recommend', __name__)

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
    liked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=1, liked=1).all()]
    disliked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=1, liked=0).all()]
    
    if (len(liked) < TAMANHO_MINIMO_SVM) or (len(disliked) < TAMANHO_MINIMO_SVM):
        list_img_ini = select_images.select_images_distance()
    else:
        list_img_ini = select_images.select_images_svm(liked, disliked)
    
    return jsonify({'img_list': list_img_ini})

@recommend.route('/recommend/best', methods=['GET'])
@login_required
def best(user):
    liked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=1, liked=1).all()]
    disliked = [p.name for p in Product.query.join(Preference,aliased=True).filter_by(user_id=1, liked=0).all()]
    
    if (len(liked) < TAMANHO_MINIMO_SVM) or (len(disliked) < TAMANHO_MINIMO_SVM):
        return jsonify({'message': 'fail'})
    else:
        return jsonify({'img': select_images.select_best_svm(liked, disliked)})
    
    