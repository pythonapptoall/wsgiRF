"""
Модуль обрабатывает GET запросы
"""

from .request_abc import RequestsABC


class GetRequests(RequestsABC):
    """
    Класс обрабатывает GET запросы и возвращает словарь с данными тела запроса

    Является наследником класса RequestsABC
    """

    @staticmethod
    def get_input_data(server_data):
        """
        Выделяет из данных, пришедших от сервера, тело запроса
        """
        return server_data['QUERY_STRING']

    def parse_input_data(self, request_data):
        """
        Распаковывает тело запроса
        """

        request_data_dic = self.parse_into_dic(request_data)
        return request_data_dic
