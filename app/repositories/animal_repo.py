from app.models.animals import Animals
from app.utils.database import db

class Animal_repo():
    
    def get_list_animals(self):
        animal = Animals.query.all()
        return animal
    
    def update_animal(self, id, animals):
        animals_obj = Animals.query.get(id)
        animals_obj.species = animals.species
        animals_obj.age = animals.age
        animals_obj.gender = animals.gender
        animals_obj.habitat = animals.habitat
        animals_obj.countries = animals.countries

        db.session.commit()
