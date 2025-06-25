import pytest
from app import app, db, Task
import os, sys
# ensure project root is on Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_and_get_task(client):
    rv = client.post('/tasks', json={'title': 'Test Task'})
    assert rv.status_code == 201
    data = rv.get_json()
    assert data['title'] == 'Test Task'
    tid = data['id']

    rv2 = client.get(f'/tasks/{tid}')
    assert rv2.status_code == 200
    assert rv2.get_json()['title'] == 'Test Task'

def test_update_and_delete_task(client):
    rv = client.post('/tasks', json={'title': 'Temp'})
    tid = rv.get_json()['id']

    rv2 = client.put(f'/tasks/{tid}', json={'done': True})
    assert rv2.status_code == 200
    assert rv2.get_json()['done'] is True

    rv3 = client.delete(f'/tasks/{tid}')
    assert rv3.status_code == 204

    rv4 = client.get(f'/tasks/{tid}')
    assert rv4.status_code == 404
