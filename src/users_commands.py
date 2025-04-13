import db

def login(username, password):
    sql = '''SELECT username, password
             FROM users
             WHERE username = ? AND
             password = ?'''
    result = db.query(sql, [username, password])
    return result[0] if result else None

def get_id(username, password):
    sql = """SELECT id
             FROM users
             WHERE username = ? AND
             password = ?"""
    result = db.query(sql, [username, password])
    return result[0] if result else None

def register(username, password):
    sql = '''INSERT INTO users (username, password)
             VALUES(?, ?)'''
    db.execute(sql, [username, password])

def get_all_users():
    sql = "SELECT * FROM users"
    result = db.query(sql)
    return result

def remove_user(username, password):
    sql = "DELETE FROM users WHERE username = ? AND password = ?"
    db.execute(sql, [username, password])

def create_table_users():
    sql = """CREATE TABLE users (
             id INTEGER PRIMARY KEY,
             username TEXT UNIQUE,
             password TEXT)"""
    db.execute(sql)

def drop_table_users():
    sql = "drop table if exists users"
    db.execute(sql)
