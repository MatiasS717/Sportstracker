import db

def login(username, password):
    sql = '''SELECT username, password 
             FROM users
             WHERE username = ? AND
             password = ?'''
    result = db.query(sql, [username, password])
    return result[0] if result else None

def register(username, password):
    sql = '''INSERT INTO users (username, password)
             VALUES(?, ?)'''
    db.execute(sql, [username, password])

def create_table():
    sql = """CREATE TABLE users (
             id INTEGER PRIMARY KEY,
             username TEXT UNIQUE,
             password TEXT)"""
    db.execute(sql)