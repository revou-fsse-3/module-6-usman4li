from app.repositories.animal_repo import Animal_repo

class Animals_service:

    def __init__(self):
        self.animal_repo = Animal_repo()

    def get_animal(self):
        animal = self.animal_repo.get_list_animals()
        return [animals.as_dict() for animals in animal]
    
    def search_animals(self, species):
        animal = self.animal_repo.search_animals(species)
        return [animals.as_dict() for animals in animal]
    
    def update_animal(self, id, animals_data_dto):
        updated_animal = self.animal_repo.update_animal(id, animals_data_dto)
        return  updated_animal.as_dict()