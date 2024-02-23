from app.models.animals import Animals
from app.utils.database import db

class Animal_repo():
    
    def get_list_animals(self):
        animal = Animals.query.all()
        return animal
    
    def create_animals(self, animals):
        db.session.add(animals)
        db.session.commit()
        return animals
    
    def update_animal(self, id, animals):
        animals_obj = Animals.query.get(id)
        animals_obj.species = animals.species
        animals_obj.age = animals.age
        animals_obj.gender = animals.gender
        animals_obj.habitat = animals.habitat
        animals_obj.countries = animals.countries

        db.session.commit()
        return animals_obj
    
    def delete_animals(self, id):
        animals_obj = Animals.query.get(id)

        db.session.delete(animals_obj)
        db.session.commit()
        return animals_obj

    def search_animals(self, species):
        animal = Animals.query.filter(Animals.species.like(f"%{species}%")).all()
        return animal