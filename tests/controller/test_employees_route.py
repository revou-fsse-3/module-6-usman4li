from app.service.employee_service import Employees_service

def test_get_employees(test_app, mocker):
    # Arrange data
    mock_employees_data = [
        {
            "id" : 1,
            "name":"Slamet",
            "age": 35,
            "gender": "male",
            "job": "Zoo Animal Nutrition"
        }
    ]
    mocker.patch.object(Employees_service, 'get_employee', return_value=mock_employees_data)

    # Action
    with test_app.test_client() as client:
        response = client.get("/employees/")

    # Assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_employees_data)
    assert response.json['data'] == mock_employees_data

def test_post_employees(test_app, mocker):
    #Arrange data
    data = {
        "id" : 1,
        "name":"Slamet",
        "age": 35,
        "gender": "male",
        "job": "Zoo Animal Nutrition"
    }
    mocker.patch.object(Employees_service, 'create_employees', return_value=data)

    #Action
    with test_app.test_client() as client:
        response = client.post("/employees/", json=data)

    #Assert
    assert response.status_code == 200

def test_put_employees_update(test_app, mocker):
    #Arrange data
    data = {
        "name":"Slamet",
        "age": 35,
        "gender": "male",
        "job": "Zoo Animal Nutrition"
    }

    mocker.patch.object(Employees_service, 'update_employee', return_value=data)

    #Action
    with test_app.test_client() as client:
        response = client.put("/employees/1", json=data)

    #Assert
        assert response.status_code == 200
    
def test_delete_employees(test_app, mocker):
    #Arrange
    expected_response = {
        "name":"Slamet",
        "age": 35,
        "gender": "male",
        "job": "Zoo Animal Nutrition"
    }

    mocker.patch.object(Employees_service, 'delete_employees', return_value=expected_response)

    #Action
    with test_app.test_client() as client:
        response = client.delete("employees/4")

    #Assert
    assert response.status_code == 200

def test_delete_employees_not_found(test_app, mocker):
    #Arrange
    expected_response = "Employees not found"

    mocker.patch.object(Employees_service, "delete_employees", return_value=expected_response)

    #Action
    with test_app.test_client() as client:
        response = client.delete("employees/5")

    #Assert
    assert response.status_code == 404
    # assert response.json['data'] == "Animals not found"