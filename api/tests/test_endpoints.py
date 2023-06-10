import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


# Тест для 'api/themes/'
@pytest.mark.django_db
def test_get_themes(client):
    response = client.get('/api/themes/')
    assert response.status_code == 200


# Тест для POST 'api/themes/<int:pk>/'
@pytest.mark.django_db
def test_theme_api_post(client):
    url = '/api/themes/'
    response = client.post(url, data={'name': "story"})
    assert response.status_code == 201


# Тест для PUT 'api/themes/<int:pk>/'
@pytest.mark.django_db
def test_theme_api_update(client):
    url = '/api/themes/1/'
    response = client.put(url, data={'name': "biology"})
    assert response.status_code == 200


# Тест для DELETE 'api/themes/delete/<int:pk>/'
@pytest.mark.django_db
def test_theme_api_destroy(client):
    url = '/api/themes/delete/1/'
    response = client.delete(url)
    assert response.status_code == 204


# Тест для GET 'api/answers/<int:pk>/'
@pytest.mark.django_db
def test_get_answers_view(client):
    url = '/api/answers/1/'
    response = client.get(url)
    assert response.status_code == 200


# Тест для GET 'api/statistic/<int:id>/'
@pytest.mark.django_db
def test_user_statistik_view(client):
    url = '/api/statistic/1/'
    response = client.get(url)
    assert response.status_code == 200
