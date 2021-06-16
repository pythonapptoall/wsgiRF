"""
Используем стандартную библиотеку "requests" для тестирования запросов. Примеры запросов:
    response = requests.get(
            request_path,
            params=get_request_param,
            )

    response = requests.post(
            request_path,
            data=post_request_param.encode("UTF-8")
            )

Варианты данных:
    response.encoding = 'utf-8'
    response.status_code
        200
    response.content:
        b'{"PATH_INFO": "/", "routes": ["/", "/post_request/", "/about/"], "date": "2021-06-08",
            "secret_key": "something", "get_request_params": {"sport": "Soccer", "function":
            "get_source_schedule", "debug": "1", "tournament_id": "4", "source_id": "6"}}'
    response.text:
        {"PATH_INFO": "/", "routes": ["/", "/post_request/", "/about/"], "date": "2021-06-08",
            "secret_key": "something", "get_request_params": {"sport": "Soccer", "function":
                "get_source_schedule", "debug": "1", "tournament_id": "4", "source_id": "6"}}
    response.json():
        {'PATH_INFO': '/', 'routes': ['/', '/post_request/', '/about/'], 'date': '2021-06-08',
            'secret_key': 'something', 'get_request_params': {'sport': 'Soccer', 'function':
            'get_source_schedule', 'debug': '1', 'tournament_id': '4', 'source_id': '6'}}
    response.headers:
        {'Date': 'Tue, 08 Jun 2021 17:48:00 GMT', 'Server': 'WSGIServer/0.2 CPython/3.9.4',
            'Content-Type': 'text/html', 'Content-Length': '245'}
"""

import requests

from .d_base_app.d_base import open_db_connection


def test_get_requests(request_path):
    """
    Набор тестов для GET запросов
    """

    get_request_param = \
        'sport=Soccer&function=get_source_schedule&debug=1&tournament_id=4&source_id=6'

    response = requests.get(
        request_path,
        params=get_request_param,
    )
    print(f'test---> GET response: {response}, путь: {request_path}')
    response.encoding = 'utf-8'
    json_response = response.json()
    assert json_response['PATH_INFO'] == '/'
    assert json_response['secret_key'] == 'something'
    assert json_response['get_request_params'] == {
        'sport': 'Soccer',
        'function': 'get_source_schedule',
        'debug': '1',
        'tournament_id': '4',
        'source_id': '6'}

    request_path += 'post_requests/'
    response = requests.get(
        request_path,
        params='',
    )
    print(f'test---> GET response: {response}, путь: {request_path}')
    response.encoding = 'utf-8'
    json_response = response.json()
    assert json_response == '404 PAGE Not Found'


def test_post_requests(request_path):
    """
    Набор тестов для POST запросов
    """

    request_path += 'post_request/'
    post_request_param = 'name=Имя на кириллице&email=test@example.com&member=yes'
    response = requests.post(request_path,
                             data=post_request_param.encode("UTF-8"))
    print(f'test---> POST response: {response}, путь: {request_path}')
    response.encoding = 'utf-8'
    json_response = response.json()
    assert json_response['PATH_INFO'] == '/post_request/'
    assert json_response['secret_key'] == 'something'
    assert json_response['post_data'] == {
        'name': 'Имя на кириллице',
        'email': 'test@example.com',
        'member': 'yes'}

    request_path += '22/'
    response = requests.post(request_path,
                             data=post_request_param.encode("UTF-8"))
    print(f'test---> POST response: {response}, путь: {request_path}')
    response.encoding = 'utf-8'
    json_response = response.json()
    assert json_response == '404 PAGE Not Found'


def test_d_base_connection():
    """
    Проверка подключения к базе данных
    """

    with open_db_connection() as cursor:
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(f"test---> Вы подключены к -  {record}")


def test_requests(request_path):
    """
    Выполнение тестов для всех типов запросов
    """

    test_get_requests(request_path)
    test_post_requests(request_path)
    test_d_base_connection()
