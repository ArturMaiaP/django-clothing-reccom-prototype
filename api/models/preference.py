from . import db
from sqlalchemy.sql import func

class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    liked = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Preference {self.user_id}>'
