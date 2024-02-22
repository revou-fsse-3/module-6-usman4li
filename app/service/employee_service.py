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
    
    def update_employee(self, id, employees_data_dto):
        updated_employee = self.employee_repo.update_employee(id, employees_data_dto)
        return  updated_employee