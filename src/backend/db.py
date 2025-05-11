import sqlite3
from config import DATABASE_FILENAME

def get_connection():
    """Luo yhteyden tietokantaan."""

    con = sqlite3.connect(DATABASE_FILENAME)
    return con

def execute(sql, params=[]):
    """Suorittaa tietokantakomennon."""

    con = get_connection()
    con.execute(sql, params)
    con.commit()
    con.close()

def query(sql, params=[]):
    """Suorittaa tietokantakyselyn."""

    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result
