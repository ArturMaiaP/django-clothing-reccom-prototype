from flask import Blueprint
from . import login_required
from .models import Product

product = Blueprint('product', __name__)

@product.route('/product', methods=['GET'])
@login_required
def list_products(user):
    return Product.query.all()
