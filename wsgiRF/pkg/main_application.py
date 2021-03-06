"""'
Основное программное ядро проекта
"""

from .common.utils import Utils, Json
from .common.debugger import Debug
from .common.logger import Logger
from .requests_app.requests_main import Requests


class ProjectMainApp:
    """
    Основное программное ядро проекта

    Получает данные среды сервера, обрабатывает их, формирует из них
    запрос для дальнейшей работы фреймворка и создает ответ серверу
    """

    def __init__(self, settings, middle_ware_list, routes_dict):
        """
        При создании экземпляра инициирует параметры работы приложения данными из файла настроек
        Также формирует список доступных middle_ware и роутов
        """
        self.settings = settings
        self.middle_ware_list = middle_ware_list
        self.routes_dict = routes_dict
        self.logger = Logger.get_logger('main')

    @Debug(critical_time=0, name='main_app.__call__')
    def __call__(
            self,
            wsgi_server_data_dictionary,
            wsgi_server_response_function):
        """
        Получает пришедшие от сервера данные и ссылку на серверную функцию для возврата ответа.

        Далее формирует и возвращает ответ на запрос.
        """

        request = self.get_request_from_server_data(
            wsgi_server_data_dictionary)

        path = request['PATH_INFO']
        request_method = request['REQUEST_METHOD']
        controller = self.get_controller_for_request(
            path=path, request_method=request_method)

        response_body = self.get_response(
            controller, request, wsgi_server_response_function)

        json_response_body = Json.dumps_into_json(response_body)
        return [bytes(json_response_body, 'utf-8')]

    def get_request_from_server_data(self, server_data):
        """
        Применяет к данным, пришедшим от сервера, фронт контроллеры и формирует окончательный запрос
        для обработки
        """

        request_parameters = Requests.parse_server_request_parameters(
            server_data)

        request = Utils.to_unit_dictionaries_in_one_dictionary(
            {'PATH_INFO': server_data['PATH_INFO']},
            {'REQUEST_METHOD': server_data['REQUEST_METHOD']},
            self.get_data_from_front_controllers(),
            request_parameters)
        return request

    def get_data_from_front_controllers(self):
        """
        Получим данные из front контроллеров для дальнейшей работы

        Данные передадутся в Page контроллер для формирования окончательного ответа
        """
        data = {}
        for controller in self.middle_ware_list:
            updated_data = controller(data)
            data = Utils.to_unit_dictionaries_in_one_dictionary(
                data, updated_data)
        return data

    def get_controller_for_request(self, path, request_method):
        """
        По значению пути из запроса и типу запроса определяет контроллер для обработки запроса
        """

        correct_path = self.check_path(path)
        return self.get_page_controller_from_route(
            route_path=correct_path, request_method=request_method)

    @staticmethod
    def check_path(path):
        """ Добавляет закрывающий слэш в конце пути, если он пропущен """

        correct_path = f'{path}/' if not path.endswith('/') else f'{path}'
        return correct_path

    def get_page_controller_from_route(self, route_path, request_method):
        """Получим контроллер для дальнейшей работы по типу запроса и пути из запроса """

        controllers_by_path = self.routes_dict[request_method]

        if route_path in controllers_by_path:
            controller = controllers_by_path[route_path]
        else:
            controller = self.routes_dict['404']['NotFound']
            self.logger.log(f'Путь {route_path} не найден')
            # print(f'log--> Путь {route_path} не найден')
        return controller

    @staticmethod
    def get_response(controller, request, response_function):
        """ Устанавливает заголовок ответа серверу и возвращает сам ответ """

        status_code, body = controller(request)

        response_function(
            status_code, [
                ('Content-Type', 'text/html')])

        return body

    def get_host(self):
        """ Вернет имя хоста, на котором работает проект """

        return self.settings['ADDRESS']['HOST']

    def get_port(self):
        """ Вернет имя порта, на котором работает проект """

        return self.settings['ADDRESS']['PORT']
