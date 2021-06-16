"""
Модуль запускает пакет тестов для проекта
"""

from copy import copy

from .pkg.tests_app import tests
from .pkg.tests_app.settings import SETTINGS
from .pkg.common.utils import Utils

TEST_SETTINGS = copy(SETTINGS)


def form_path_for_test():
    """
    Создает путь для отправки запросов на сервер нашего проекта
    """

    host = TEST_SETTINGS['ADDRESS']['HOST']
    port = TEST_SETTINGS['ADDRESS']['PORT']

    return f"http://{Utils.get_host_name(host)}:{port}/"


TEST_PATH = form_path_for_test()

tests.test_requests(TEST_PATH)
