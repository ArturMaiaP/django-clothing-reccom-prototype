def get_user_by_id(db, id):
    cur = db.cursor()
    cur.execute("SELECT * FROM user WHERE id=%s", (id,))
    user = cur.fetchone()
    cur.close()
    return user

def get_user_by_email(db, email):
    cur = db.cursor()
    cur.execute("SELECT * FROM user WHERE email=%s", (email,))
    user = cur.fetchone()
    cur.close()
    return user

def insert_user(db, email, hashed, name):
    cur = db.cursor()
    cur.execute("INSERT INTO user SET email=%s, password=%s, name=%s", (email, hashed, name))
    db.commit()