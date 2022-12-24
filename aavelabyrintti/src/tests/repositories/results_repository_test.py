import unittest
from repositories.results_repository import results_repository
from init_db import initialize_database

class TestResultsRepository(unittest.TestCase):
    def setUp(self):
        self.test_results_repository = results_repository
        initialize_database()

    def test_add_results_to_database(self):
        self.test_results_repository.add_result_to_database("Testi", 30)
        self.assertEqual(len(self.test_results_repository.get_sorted_results()), 1)

    def test_sort_results(self):
        self.test_results_repository.add_result_to_database("Testi", 30)
        self.test_results_repository.add_result_to_database("Testi", 50)
        self.assertEqual(self.test_results_repository.get_sorted_results()[0][1], 50)
