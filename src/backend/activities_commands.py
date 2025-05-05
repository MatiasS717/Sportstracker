import backend.db

def add_activity(activity, tracker, training_type, user_id):
    sql = '''INSERT INTO activities (activity, tracker, training_type, user_id)
             VALUES(?, ?, ?, ?)'''
    backend.db.execute(sql, [activity, tracker, training_type, user_id])

def get_activities(user_id):
    sql = "SELECT * FROM activities WHERE user_id = ?"
    result = backend.db.query(sql, [user_id])
    return result

def delete_activity(activity, tracker, training_type, user_id):
    sql = """DELETE FROM activities WHERE
             activity = ? AND
             tracker = ? AND
             training_type = ? AND
             user_id = ?"""
    backend.db.execute(sql, [activity, tracker, training_type, user_id])

def create_table_activities():
    sql = """CREATE TABLE activities (
             id INTEGER PRIMARY KEY,
             activity TEXT,
             tracker INTEGER,
             training_type TEXT,
             user_id INTEGER REFERENCES users)
             """
    backend.db.execute(sql)

def drop_table_activities():
    sql = "drop table if exists activities"
    backend.db.execute(sql)
