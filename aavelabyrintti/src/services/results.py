from repositories.results_repository import results_repository

class Results():
    def __init__(self):
        self.results_repository = results_repository

    def add_result(self, name, result):
        self.results_repository.add_result_to_database(name, result)

    def sorted_results(self):
        return self.results_repository.get_sorted_results()