from db import connection
from init_db import initialize_database

def add_result_to_database(name, moves):
    """Lisää tuloksen tietokantaan.
    
    Args:
        name: pelaajan nimi.
        moves: siirtojen määrä.

    """

    initialize_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO results VALUES (?, ?)", (name, moves))
    connection.commit()

def get_sorted_results():
    """Järjestää tulokset siirtojen perusteella pienimmästä suurimpaan.

    Returns: Tulokset järjestyksessä.

    """
    
    cursor = connection.cursor()
    results = cursor.execute("SELECT name, result FROM results").fetchall()
    results.sort(key=lambda result:result[1])

    return results
