from app.controller.employees.schema.update_employees_request import Update_employees_request
from app.models.employees import Employees
from app.repositories.employee_repo import Employee_repo
from app.service.employee_service import Employees_service

def test_get_list_employees(test_app, mocker):
    # Arrange data
    mock_employees_data = [
        Employees(
            id=1,
            name='Slamet',
            age=35,
            gender='male',
            job='Zoo Animal Nutrition'
        ),
    ]
    mocker.patch.object(Employee_repo, 'get_list_employees', return_value=mock_employees_data)

    # Action
    with test_app.test_request_context():
        employee_service = Employees_service().get_employee()
    
    # Assert
    assert len(employee_service) == 1
    assert employee_service[0]['name'] == 'Slamet'

def test_create_employees_success(test_app, mocker):
    """service get employees success"""

    # Arrange data
    mock_employees_data = Employees(
        id=1,
        name='Slamet',
        age=35,
        gender='male',
        job='Zoo Animal Nutrition'
    )
    mocker.patch.object(Employee_repo, 'create_employees', return_value=mock_employees_data)
    Update_dto = Update_employees_request(
        name='Slamet',
        age=35,
        gender='male',
        job='Zoo Animal Nutrition'
    )

    # Action
    with test_app.test_request_context():
        employee_service_create = Employees_service().create_employees(Update_dto) 

    # Assert
    assert employee_service_create['id'] == 1
    assert employee_service_create['name'] == 'Slamet'
    assert employee_service_create['age'] == 35
    assert employee_service_create['gender'] == 'male'
    assert employee_service_create['job'] == 'Zoo Animal Nutrition'
    