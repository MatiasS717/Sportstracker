import backend.users_commands
import backend.activities_commands

def initialize_database():
    """Luo tietokannan,sekä taulut users ja activities. 
    Tietokannan ollessa olemassa, poistaa taulut users ja activities, sekä luo ne uudelleen."""
    
    backend.users_commands.drop_table_users()
    backend.activities_commands.drop_table_activities()
    backend.users_commands.create_table_users()
    backend.activities_commands.create_table_activities()

if __name__ == "__main__":
    initialize_database()
