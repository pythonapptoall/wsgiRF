"""
Модуль запускает проект.

Создает экземпляр класса движка проекта, инициирует его параметры данными из файла настроек проекта.

Далее получает из файла настроек проекта путь для запуска проекта, и запускает сервер
с выводом сообщения о запуске
"""

from copy import copy
from wsgiref.simple_server import make_server

from pkg.common.settings import SETTINGS
from pkg.common.utils import Utils
from pkg.main_application import ProjectMainApp
from pkg.common.logger import Logger


def get_project_settings(settings):
    """
    Возвращает копию файла настроек проекта.

    Копия нужна для исключения случайных изменений в головном файле настроек
    """

    return copy(settings)


def get_host_name(host):
    """
    При пустом значении имени хоста сервер запускается на хосте
    по умолчанию - localhost. Учтем это при выводе сервисного уведомления
    """

    return host if host != '' else 'localhost'


def run_wsgi_server(project_settings):
    """
    передает серверу наш движок для обмена информацией и адрес запуска из настроек.
    после запускает сервер
    """

    application = ProjectMainApp(project_settings)

    host = project_settings['ADDRESS']['HOST']
    port = project_settings['ADDRESS']['PORT']

    with make_server(host, port, application) as httpd:
        display_server_message(host=host, port=port)
        httpd.serve_forever()


def display_server_message(host, port):
    """ выводит сервисное сообщение о запуске сервера """
    host_name = get_host_name(host)
    logger.log(f"Serving on {host_name}:{port}...")


if __name__ == '__main__':
    PROJECT_SETTINGS = get_project_settings(SETTINGS)

    Utils.set_project_modules_relative_import_paths()

    logger = Logger.get_logger()

    run_wsgi_server(PROJECT_SETTINGS)
