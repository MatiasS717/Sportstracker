import backend.users_commands
import backend.activities_commands

def initialize_database():
    backend.users_commands.drop_table_users()
    backend.activities_commands.drop_table_activities()
    backend.users_commands.create_table_users()
    backend.activities_commands.create_table_activities()

if __name__ == "__main__":
    initialize_database()
