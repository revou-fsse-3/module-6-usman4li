from flask import Blueprint, request
from app.utils.database import db
from app.models.animals import Animals
from app.utils.api_response import api_response
from app.service.animal_service import Animals_service

animals_blueprint = Blueprint('animals_endpoint', __name__)

@animals_blueprint.route("/", methods=["GET"])
def get_list_animals():
    try:
        animals_service = Animals_service()

        animal = animals_service.get_animal()
        
        # return [animals.as_dict() for animals in animal], 200
        return api_response(
            status_code=200,
            message="",
            data=animal
        )
    
    except Exception as e:
        return {"error": str(e)}, 500

@animals_blueprint.route("/<int:animals_id>", methods=["GET"])
def get_animals(animals_id):
    try:

        animals = Animals.query.get(animals_id)

        if not animals:
            return "Animal not found", 404
        
        return animals.as_dict(), 200
    except Exception as e:
        return {"error": str(e)}, 500

@animals_blueprint.route("/", methods=["POST"])
def create_animals():
    try:
        data = request.json

        animals = Animals()
        animals.species = data["species"]
        animals.age = data["age"]
        animals.gender = data["gender"]
        animals.habitat = data["habitat"]
        animals.countries = data["countries"]
        db.session.add(animals)
        db.session.commit()
        return "berhasil", 200
    except Exception as e:
        return {"error": str(e)}, 500

@animals_blueprint.route("/<int:animals_id>", methods=["PUT"])
def update_animals(animals_id):
    try:


        data = request.json

        animals = Animals()
        animals.species = data.get("species", animals.species)
        animals.age = data.get("age", animals.age)
        animals.gender = data.get("gender", animals.gender)
        animals.habitat = data.get("habitat", animals.habitat)
        animals.countries = data.get("countries", animals.countries)
        
        animals_service = Animals_service()

        animals = animals_service.update_animal(animals_id,animals)

        db.session.commit()

        return api_response(
            status_code=200,
            message="",
            data=animals
        )
    except Exception as e:
        return {"error": str(e)}, 500


