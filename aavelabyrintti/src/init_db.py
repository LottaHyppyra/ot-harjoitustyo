from db import connection

def empty_db():
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS results
    """)

    connection.commit()

def create_tables():
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            name TEXT,
            result INTEGER
        );
    """)

    connection.commit()

def initialize_database():
    create_tables()

if __name__ == "__main__":
    initialize_database()
