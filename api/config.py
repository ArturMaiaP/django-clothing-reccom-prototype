import os

SECRET_KEY = os.getenv('SECRET_KEY') or 'secret'
DEBUG = os.getenv("DEBUG") or False

MYSQL_DATABASE_HOST = os.getenv("MYSQL_DATABASE_HOST") or "localhost"
MYSQL_DATABASE_PORT = os.getenv("MYSQL_DATABASE_PORT") or 3306
MYSQL_DATABASE_USER = os.getenv("MYSQL_DATABASE_USER") or "user"
MYSQL_DATABASE_PASSWORD = os.getenv("MYSQL_DATABASE_PASSWORD") or "secret"
MYSQL_DATABASE_DB = os.getenv("MYSQL_DATABASE_DB") or "database"
