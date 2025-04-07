import db

def add_activity(activity, tracker, training_type, user_id):
    sql = '''INSERT INTO activities (activity, tracker, training_type, user_id)
             VALUES(?, ?, ?, ?)'''
    db.execute(sql, [activity, tracker, training_type, user_id])

def create_table_activities():
    sql = """CREATE TABLE activities (
             id INTEGER PRIMARY KEY,
             activity TEXT,
             tracker INTEGER,
             training_type TEXT,
             user_id INTEGER REFERENCES users)
             """
    db.execute(sql)