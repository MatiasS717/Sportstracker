import backend.db

def login(username, password):
    """Tarkistaa käyttäjän kirjautumistiedot tietokannasta."""

    sql = '''SELECT username, password
             FROM users
             WHERE username = ? AND
             password = ?'''
    result = backend.db.query(sql, [username, password])
    return result[0] if result else None

def get_id(username, password):
    """Hakee käyttäjän id-numeron tietokannasta."""

    sql = """SELECT id
             FROM users
             WHERE username = ? AND
             password = ?"""
    result = backend.db.query(sql, [username, password])
    return result[0] if result else None

def register(username, password):
    """Lisää käyttäjän tietokantaan."""

    sql = '''INSERT INTO users (username, password)
             VALUES(?, ?)'''
    backend.db.execute(sql, [username, password])

def get_all_users():
    """Hakee kaikki käyttäjät tietokannasta."""

    sql = "SELECT * FROM users"
    result = backend.db.query(sql)
    return result

def remove_user(username, password):
    """Poistaa käyttäjän tietokannasta."""

    sql = "DELETE FROM users WHERE username = ? AND password = ?"
    backend.db.execute(sql, [username, password])

def create_table_users():
    """Luo tietokantaan taulun users."""

    sql = """CREATE TABLE users (
             id INTEGER PRIMARY KEY,
             username TEXT UNIQUE,
             password TEXT)"""
    backend.db.execute(sql)

def drop_table_users():
    """Poistaa tietokannasta taulun users."""

    sql = "drop table if exists users"
    backend.db.execute(sql)
