from db import connection

class Results_repository():
    """Tulosten tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: tietokantayhteys
        """
        
        self.cursor = connection.cursor()
        self.connection = connection

    def add_result_to_database(self, name, moves):
        """Lisää tuloksen tietokantaan.
        
        Args:
            name: pelaajan nimi.
            moves: siirtojen määrä.

        """

        self.cursor.execute("INSERT INTO results VALUES (?, ?)", (name, moves))
        self.connection.commit()

    def get_sorted_results(self):
        """Järjestää tulokset siirtojen perusteella pienimmästä suurimpaan.

        Returns: Tulokset järjestyksessä.

        """

        results = self.cursor.execute("SELECT name, result FROM results").fetchall()
        results.sort(key=lambda result:result[1])

        return results

results_repository = Results_repository(connection)
