from app.utils.database import db

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(100), nullable=False)
    habitat = db.Column(db.String(100), nullable=False)
    countries = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "species": self.species,
            "age": self.age,
            "gender": self.gender,
            "habitat": self.habitat,
            "countries": self.countries
            }