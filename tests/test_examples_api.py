from http import HTTPStatus

def test_long_task(client):
    response = client.get('/long-task')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Tarefa concluída!"}
