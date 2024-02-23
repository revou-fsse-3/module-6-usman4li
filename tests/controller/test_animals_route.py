
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
