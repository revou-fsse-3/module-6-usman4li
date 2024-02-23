from app.models.animals import Animals
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
    
    def create_animals(self, animals_data_dto):
        animals = Animals()

        animals.species = animals_data_dto.species
        animals.age = animals_data_dto.age
        animals.gender = animals_data_dto.gender
        animals.habitat = animals_data_dto.habitat
        animals.countries = animals_data_dto.countries

        created_animals = self.animal_repo.create_animals(animals)
        return created_animals.as_dict()

    def update_animal(self, id, animals_data_dto):
        updated_animal = self.animal_repo.update_animal(id, animals_data_dto)
        return  updated_animal.as_dict()
    
    def delete_animals(self, id):
        animals = Animals.query.get(id)
        if not animals:
            return "Animals not found"
        
        deleted_animals = self. animal_repo.delete_animals(id)
        return deleted_animals.as_dict()