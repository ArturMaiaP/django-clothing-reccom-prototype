from . import db
from sqlalchemy.sql import func

class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    preferences = db.relationship("Preference")
    
    def __repr__(self):
        return f'<User {self.name}>'