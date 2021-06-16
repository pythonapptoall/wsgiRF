"""
Модуль запускает проект.

Создает экземпляр класса движка проекта, инициирует его параметры данными из файла настроек проекта.

Далее получает из файла настроек проекта путь для запуска проекта, и запускает сервер
с выводом сообщения о запуске
"""

from copy import copy
from wsgiref.simple_server import make_server

from .pkg.common.utils import Utils
from .pkg.main_application import ProjectMainApp
from .pkg.common.logger import Logger


class RunServer:
    def __init__(self, settings, middle_ware_list, routes_dict):
        """

        """

        self.settings = self.get_project_settings(settings)
        self.logger = Logger.start_logger('main')
        self.application = ProjectMainApp(settings=self.settings,
                                          middle_ware_list=middle_ware_list,
                                          routes_dict=routes_dict)

    def __call__(self):
        """

        """

        self.run_wsgi_server()

    @staticmethod
    def get_project_settings(settings):
        """
        Возвращает копию файла настроек проекта.
    
        Копия нужна для исключения случайных изменений в головном файле настроек
        """

        return copy(settings)

    def run_wsgi_server(self):
        """
        передает серверу wsgiref.simple_server наш движок для обмена информацией 
        и адрес запуска из настроек. После запускает сервер
        """

        host = self.settings['ADDRESS']['HOST']
        port = self.settings['ADDRESS']['PORT']
        application = self.application

        with make_server(host, port, application) as httpd:
            self.display_server_message(host=host, port=port)
            httpd.serve_forever()

    def display_server_message(self, host, port):
        """ выводит сервисное сообщение о запуске сервера """
        host_name = Utils.get_host_name(host)
        self.logger.log(f"Serving on {host_name}:{port}...")
