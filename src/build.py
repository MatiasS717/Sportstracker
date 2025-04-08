import users_commands
import activities_commands

def initialize_database():
    users_commands.create_table_users()
    activities_commands.create_table_activities()

if __name__ == "__main__":
    initialize_database()
