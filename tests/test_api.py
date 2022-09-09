import json
import pytest
from app import app


keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


# tests for api
def test_api_posts():
    response = app.test_client().get('/api/posts')
    data = response.json
    keys = set((response.json[0]).keys())

    assert response.status_code == 200, 'Возвращается неверный код'
    assert type(data) == list, 'Должен возвращаться список'
    assert keys == keys_should_be, "Возвращаемые ключи не совпадают с заданными"


def test_api_certain_post():
    response = app.test_client().get('/api/posts/1')
    data = response.json
    keys = set(response.json.keys())

    assert response.status_code == 200, 'Возвращается неверный код'
    assert type(data) == dict, 'Должен возвращаться словарь'
    assert keys == keys_should_be, "Возвращаемые ключи не совпадают с заданными"
