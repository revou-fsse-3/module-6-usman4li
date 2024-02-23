from flask import Blueprint, request
from app.controller.animals.schema.update_animals_request import Update_animals_request
from app.utils.database import db
from app.models.animals import Animals
from app.utils.api_response import api_response
from app.service.animal_service import Animals_service
from pydantic import ValidationError

animals_blueprint = Blueprint('animals_endpoint', __name__)

@animals_blueprint.route("/", methods=["GET"])
def get_list_animals():
    try:
        animals_service = Animals_service()

        animal = animals_service.get_animal()
        
        return api_response(
            status_code=200,
            message="",
            data=animal
        )
    
    except Exception as e:
        return api_response(
            status_code=500,
            message={"error": str(e)},
            data={}
        )
    
@animals_blueprint.route("/search", methods=["GET"])
def search_animals():
    try:
        request_data = request.args
        animals_service = Animals_service()

        animal = animals_service.search_animals(request_data["species"])
        
        return api_response(
            status_code=200,
            message="",
            data=animal
        )
    
    except Exception as e:
        return api_response(
            status_code=500,
            message={"error": str(e)},
            data={}
        )

@animals_blueprint.route("/<int:animals_id>", methods=["GET"])
def get_animals(animals_id):
    try:

        animals = Animals.query.get(animals_id)

        if not animals:
            return "Animal not found", 404
        
        return animals.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message={"error": str(e)},
            data={}
        )

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
    
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message={"error": str(e)},
            data={}
        )

@animals_blueprint.route("/<int:animals_id>", methods=["PUT"])
def update_animals(animals_id):
    try:

        data = request.json
        update_animals_request = Update_animals_request(**data)
 
        animals = Animals()
        # animals.species = data.get("species", animals.species)
        # animals.age = data.get("age", animals.age)
        # animals.gender = data.get("gender", animals.gender)
        # animals.habitat = data.get("habitat", animals.habitat)
        # animals.countries = data.get("countries", animals.countries)
        animals.species = update_animals_request.species
        animals.age = update_animals_request.age
        animals.gender = update_animals_request.gender
        animals.habitat = update_animals_request.habitat
        animals.countries = update_animals_request.countries
        
        animals_service = Animals_service()

        animals = animals_service.update_animal(animals_id,animals)

        db.session.commit()

        return api_response(
            status_code=200,
            message="updated",
            data=animals
        )
    
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message={"error": str(e)},
            data={}
        )


@animals_blueprint.route("/<int:animals_id>", methods=["DELETE"])
def delete_animals(animals_id):
    try:
        animals = Animals.query.get(animals_id)

        if not animals:
            return "Animals not found", 404
        
        db.session.delete(animals)
        db.session.commit()

        return "Delete successful", 200
    except Exception as e:
        # return {"error": str(e)}, 500
        return api_response(
            status_code=500,
            message={"error": str(e)},
            data={}
        )