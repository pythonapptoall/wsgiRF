"""
Абстрактный класс-родитель для создания классов-обработчиков запросов разного типа

Содержит типовые элементы, чтобы не дублировать код проекта. Классы для разных типов запросов
наследуются от данного класса
"""


class RequestsABC:
    """
    Абстрактный клас для создания обработчиков запросов GET и POST.

    Содержит общий функционал для работы с запросами
    """

    def get_request_params(self, server_data):
        """
        Получает необработанные данные от сервера, выделяет из них запрос и
        превращает данные запроса в словарь Python
        """

        request_data = self.get_input_data(server_data)
        request_data_dic = self.parse_input_data(request_data)

        return request_data_dic

    @staticmethod
    def get_input_data(server_data):
        """
        Выделяет из данных, пришедших от сервера, тело запроса
        """

    def parse_input_data(self, request_data):
        """
        Распаковывает тело запроса
        """

    @staticmethod
    def parse_into_dic(request_data: str):
        """
        Переводит данные из тела запроса в словарь Python
        """

        request_data_dic = {}
        if request_data:
            request_params = request_data.split('&')
            for param in request_params:
                param_key, param_value = param.split('=')
                request_data_dic[param_key] = param_value
        return request_data_dic
