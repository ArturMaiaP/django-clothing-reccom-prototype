
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import *
from .product import *
from .preference import *
from .chat import *
from .finish import *
from .logs import *