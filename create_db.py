from dataclasses import dataclass
import pymysql
import os
from dotenv import load_dotenv
load_dotenv('.env')

db = pymysql.connect(
    host=os.getenv("MYSQL_DATABASE_HOST") or "localhost",
    port=os.getenv("MYSQL_DATABASE_PORT") or 3306,
    user=os.getenv("MYSQL_DATABASE_USER") or "user",
    password=os.getenv("MYSQL_DATABASE_PASSWORD") or "secret",
    database=os.getenv("MYSQL_DATABASE_DB") or "database"
)

cur = db.cursor()
cur.execute("CREATE TABLE user (id INT(11) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL);")