from . import db
from sqlalchemy.sql import func

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    session = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Chat {self.id}>'
