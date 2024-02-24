from app.models.employees import Employees
from app.repositories.employee_repo import Employee_repo

class Employees_service:

    def __init__(self):
        self.employee_repo = Employee_repo()

    def get_employee(self):
        employee = self.employee_repo.get_list_employees()
        return [employees.as_dict() for employees in employee]
    
    def search_employees(self, name):
        employee = self.employee_repo.search_employees(name)
        return [employees.as_dict() for employees in employee]
    
    def create_employees(self, employees_data_dto):
        employees = Employees()

        employees.name = employees_data_dto.name
        employees.age = employees_data_dto.age
        employees.gender = employees_data_dto.gender
        employees.job = employees_data_dto.job

        create_employees = self.employee_repo.create_employees(employees)
        return create_employees.as_dict()
    
    def update_employee(self, id, employees_data_dto):
        updated_employee = self.employee_repo.update_employee(id, employees_data_dto)
        return  updated_employee
    
    def delete_employees(self, id):
        employees = Employees.query.get(id)
        if not employees:
            return "Employees not found"
        
        deleted_employees = self.employee_repo.delete_employees(id)
        return deleted_employees.as_dict()