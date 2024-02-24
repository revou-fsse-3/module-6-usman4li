
from app.service.animal_service import Animals_service

def test_get_animals(test_app, mocker):
    # Arrange data
    mock_animals_data = [
        {
            "id" : 4,
            "species" : "Giraffe",
            "age" : 3,
            "gender" : "male",
            "habitat": "Savannahs and Woodlands",
            "countries": "africa"
        }
    ]
    mocker.patch.object(Animals_service, 'get_animal', return_value=mock_animals_data)

    # Action
    with test_app.test_client() as client:
        response = client.get("/animals/")

    # Assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_animals_data)
    assert response.json['data'] == mock_animals_data

def test_post_animals(test_app, mocker):
    #Arrange data
    data = {
        "id" : 4,
        "species" : "Giraffe",
        "age" : 3,
        "gender" : "male",
        "habitat": "Savannahs and Woodlands",
        "countries": "africa"
    }
    mocker.patch.object(Animals_service, 'create_animals', return_value=data)

    #Action
    with test_app.test_client() as client:
        response = client.post("/animals/", json=data)

    #Assert
    assert response.status_code == 200

def test_put_animals_update(test_app, mocker):
    #Arrange data
    data = {
        "species":"Lion",
        "age": 2,
        "gender": "female",
        "habitat": "Savannahs and Woodlands",
        "countries": "africa"
    }

    mocker.patch.object(Animals_service, 'update_animal', return_value=data)

    #Action
    with test_app.test_client() as client:
        response = client.put("/animals/2", json=data)

    #Assert
        assert response.status_code == 200

def test_delete_animals(test_app, mocker):
    #Arrange
    expected_response = {
        "species" : "Giraffe",
        "age" : 3,
        "gender" : "male",
        "habitat": "Savannahs and Woodlands",
        "countries": "africa"
    }

    mocker.patch.object(Animals_service, 'delete_animals', return_value=expected_response)

    #Action
    with test_app.test_client() as client:
        response = client.delete("animals/31")

    #Assert
    assert response.status_code == 200

def test_delete_animals_not_found(test_app, mocker):
    #Arrange
    expected_response = "Animals not found"

    mocker.patch.object(Animals_service, "delete_animals", return_value=expected_response)

    #Action
    with test_app.test_client() as client:
        response = client.delete("animals/20")

    #Assert
    assert response.status_code == 404
    # assert response.json['data'] == "Animals not found"