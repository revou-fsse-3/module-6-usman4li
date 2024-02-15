from flask import Blueprint
from app.utils.database import db
from app.models.animals import Animals

animals_blueprint = Blueprint('animals_endpoint', __name__)

@animals_blueprint.route("/", methods=["POST"])
def create_animals():
    try:
        animals = Animals()
        animals.species = "Elepant"
        animals.age = 2
        animals.gender = "male"
        animals.habitat = "forest"
        animals.countries = "thailand"
        db.session.add(animals)
        db.session.commit()
        return "berhasil", 200
    except Exception as e:
        return e, 500

