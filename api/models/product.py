from . import db
from sqlalchemy.sql import func


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    x = db.Column(db.Numeric(20, 8), nullable=False)
    y = db.Column(db.Numeric(20, 8), nullable=False)
    a_line = db.Column(db.Boolean(), nullable=True)
    denim = db.Column(db.Boolean(), nullable=True)
    dots = db.Column(db.Boolean(), nullable=True)
    faux = db.Column(db.Boolean(), nullable=True)
    faux_leather = db.Column(db.Boolean(), nullable=True)
    Floral = db.Column(db.Boolean(), nullable=True)
    knit = db.Column(db.Boolean(), nullable=True)
    Lacy = db.Column(db.Boolean(), nullable=True)
    leather = db.Column(db.Boolean(), nullable=True)
    maxi = db.Column(db.Boolean(), nullable=True)
    midi = db.Column(db.Boolean(), nullable=True)
    mini = db.Column(db.Boolean(), nullable=True)
    pencil = db.Column(db.Boolean(), nullable=True)
    Pleated = db.Column(db.Boolean(), nullable=True)
    Printed = db.Column(db.Boolean(), nullable=True)
    skater = db.Column(db.Boolean(), nullable=True)
    Stripes = db.Column(db.Boolean(), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Product {self.name}>'
