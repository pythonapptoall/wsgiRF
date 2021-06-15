"""
Модуль содержит декораторы для формирования роутеров приложения
"""

from ...common.logger import Logger

LOGGER = Logger.get_logger()


class AppRoutes:
    """
    Используется как родительский класс декораторов page контроллеров,
    которые должны попасть в роутинг.

    Пример использования:
        class AppRoute(AppRoutes):
            ....

        @AppRoute(route="/about/")
    Формирует на уровне класса AppRoutes словарь routes, содержащий соответствие роутера и
    контроллера для его обработки:
        {
            'GET': {
                '/': IndexPage(),
                '/about/': AboutPage(),
            }
            'POST': {
                '/post_request/': PostRequest(),
            }
        }
    Через @classmethod собирает роутеры со всех экземпляров класса в один словарь
    """

    request_type = ''
    routes = {}

    def __init__(self, route):
        """
        Сохраняем значение переданного параметра
        """

        self.route = route
        self.add_request_type_to_route()

    def __call__(self, cls):
        """
        Сам декоратор
        """

        self.add_into_routes(self.request_type, self.route, cls())

    def add_request_type_to_route(self):
        """
        Если данный тип запросов не зарегистрирован в роутерах, то добавим. Для этого
        добавляем в роутеры пустой словарь по ключу, равному типу запроса
        """

        if self.request_type not in self.routes:
            self.routes[self.request_type] = {}

    @classmethod
    def add_into_routes(cls, request_type, route, ctrl):
        """
        Добавляет из экземпляра класса в переменную класса соответствие
        роутера и контроллера
        """

        cls.routes[request_type][route] = ctrl

    @classmethod
    def get_page_controller_from_route(cls, route_path, request_method):
        """Получим контроллер для дальнейшей работы по типу запроса и пути из запроса """

        controllers_by_path = cls.routes[request_method]

        if route_path in controllers_by_path:
            controller = controllers_by_path[route_path]
        else:
            controller = cls.routes['404']['NotFound']
            LOGGER.log(f'Путь {route_path} не найден')
        return controller


class GetRequest(AppRoutes):
    """
    Используется как декоратор page контроллеров, которые используются при GET запросах
    """

    def __init__(self, route):
        """
        Сохраняем значение переданного параметра
        """

        self.request_type = 'GET'
        super().__init__(route)


class PostRequest(AppRoutes):
    """
    Используется как декоратор page контроллеров, которые используются при POST запросах
    """

    def __init__(self, route):
        """
        Сохраняем значение переданного параметра
        """

        self.request_type = 'POST'
        super().__init__(route)


class NotFoundRequest(AppRoutes):
    """
    Используется как декоратор page контроллеров, которые используются при GET запросах
    """

    def __init__(self, route):
        """
        Сохраняем значение переданного параметра
        """

        self.request_type = '404'
        super().__init__(route)
