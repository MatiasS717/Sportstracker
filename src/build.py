import sql_commands

def initialize_database():
    sql_commands.create_table()

if __name__ == "__main__":
    initialize_database()