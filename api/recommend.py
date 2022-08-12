from flask import Blueprint
from . import login_required

recommend = Blueprint('recommend', __name__)

@recommend.route('/like', methods=['POST'])
@login_required
def like(user):
    return 'Like'

@recommend.route('/dislike', methods=['POST'])
@login_required
def dislike(user):
    return 'Dislike'

@recommend.route('/recommend', methods=['POST'])
@login_required
def recomm(user):
    return 'Recommend'