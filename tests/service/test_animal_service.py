from app.controller.animals.schema.update_animals_request import Update_animals_request
from app.models.animals import Animals
from app.service.animal_service import Animals_service
from app.repositories.animal_repo import Animal_repo

def test_get_list_animals(test_app, mocker):
    # Arrange data
    mock_animals_data = [
        Animals(
            id=2,
            species='Lion',
            age=2,
            gender='female',
            habitat='Savannahs and Woodlands',
            countries='africa'
            ),
    ]
    mocker.patch.object(Animal_repo, 'get_list_animals', return_value=mock_animals_data)

    # Action
    with test_app.test_request_context():
        animal_service = Animals_service().get_animal()
    
    # Assert
    assert len(animal_service) == 1
    assert animal_service[0]['species'] == 'Lion'

def test_create_animals_success(test_app, mocker):
    """service get animals success"""

    # Arrange data
    mock_animals_data = Animals(
        id=2,
        species='Lion',
        age=2,
        gender='female',
        habitat='Savannahs and Woodlands',
        countries='africa'
    )
    mocker.patch.object(Animal_repo, 'create_animals', return_value=mock_animals_data)
    Update_dto = Update_animals_request(
        species='Lion',
        age=2,
        gender='female',
        habitat='Savannahs and Woodlands',
        countries='africa'
    )

    # Action
    with test_app.test_request_context():
        animal_service_create = Animals_service().create_animals(Update_dto) 

    # Assert
    assert animal_service_create['id'] == 2
    assert animal_service_create['species'] == 'Lion'
    assert animal_service_create['age'] == 2
    assert animal_service_create['gender'] == 'female'
    assert animal_service_create['habitat'] == 'Savannahs and Woodlands'
    assert animal_service_create['countries'] == 'africa'

    