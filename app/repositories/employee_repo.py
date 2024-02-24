from app.models.employees import Employees
from app.utils.database import db

class Employee_repo():
    
    def get_list_employees(self):
        employee = Employees.query.all()
        return employee
    
    def create_employees(self, employess):
        db.session.add(employess)
        db.session.commit()
        return employess
    
    def update_employee(self, id, employees):
        employees_obj = Employees.query.get(id)
        employees_obj.name = employees.name
        employees_obj.age = employees.age
        employees_obj.gender = employees.gender
        employees_obj.job = employees.job

        db.session.commit()

    def delete_employees(self, id):
        employees_obj = Employees.query.get(id)
        db.session.delete(employees_obj)
        db.session.commit()
        
    def search_employees(self, name):
        employee = Employees.query.filter(Employees.name.like(f"%{name}%")).all()
        return employee