import backend.users_commands
import backend.activities_commands

def initialize_database():
    users_commands.drop_table_users()
    activities_commands.drop_table_activities()
    users_commands.create_table_users()
    activities_commands.create_table_activities()

if __name__ == "__main__":
    initialize_database()
