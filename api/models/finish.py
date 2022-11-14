from . import db
from sqlalchemy.sql import func

class Finish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    
    def __repr__(self):
        return f'<Finish {self.user_id},{self.product_id}>'
