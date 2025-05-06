import sqlite3

def get_connection():
    """Luo yhteyden tiedostoon database.db."""

    con = sqlite3.connect("database.db")
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
