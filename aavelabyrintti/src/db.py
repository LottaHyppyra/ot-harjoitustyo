import sqlite3

DATABASE = 'database.db'

def get_db_connection():
    path = DATABASE
    con = sqlite3.connect(path)
    return con

connection = get_db_connection()