from flask import Blueprint, request
from app.utils.database import db
from app.models.employees import Employees
from app.utils.api_response import api_response
from app.service.employee_service import Employees_service

employees_blueprint = Blueprint('employees_endpoint', __name__)

@employees_blueprint.route("/", methods=["GET"])
def get_list_employees():
    try:
        employees_service = Employees_service()

        employee = employees_service.get_employee()
        
        return api_response(
            status_code=200,
            message="",
            data=employee
        )
    
    except Exception as e:
        return {"error": str(e)}, 500
    
@employees_blueprint.route("/search", methods=["GET"])
def search_employees():
    try:
        request_data = request.args
        employees_service = Employees_service()

        employee = employees_service.search_employees(request_data["name"])
        
        return api_response(
            status_code=200,
            message="",
            data=employee
        )
    
    except Exception as e:
        return {"error": str(e)}, 500

@employees_blueprint.route("/<int:employees_id>", methods=["GET"])
def get_employees(employees_id):
    try:

        employees = Employees.query.get(employees_id)

        if not employees:
            return "Employee not found", 404
        
        return employees.as_dict(), 200
    except Exception as e:
        return {"error": str(e)}, 500

@employees_blueprint.route("/", methods=["POST"])
def create_employees():
    try:
        data = request.json

        employees = Employees()
        employees.name = data["name"]
        employees.age = data["age"]
        employees.gender = data["gender"]
        employees.job = data["job"]
        db.session.add(employees)
        db.session.commit()
        return "berhasil", 200
    except Exception as e:
        return {"error": str(e)}, 500

@employees_blueprint.route("/<int:employees_id>", methods=["PUT"])
def update_employees(employees_id):
    try:


        data = request.json
 
        employees = Employees()
        employees.name = data.get("name", employees.name)
        employees.age = data.get("age", employees.age)
        employees.gender = data.get("gender", employees.gender)
        employees.job = data.get("job", employees.job)
        
        employees_service = Employees_service()

        employees = employees_service.update_employee(employees_id,employees)

        db.session.commit()

        return api_response(
            status_code=200,
            message="",
            data=employees
        )
    except Exception as e:
        return {"error": str(e)}, 500

@employees_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employees(employee_id):
    try:
        employees = Employees.query.get(employee_id)

        if not employees:
            return "Employee not found", 404
        
        db.session.delete(employees)
        db.session.commit()

        return "Delete successful", 200
    except Exception as e:
        return {"error": str(e)}, 500
