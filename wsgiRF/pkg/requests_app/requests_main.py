"""
Центральный модуль обработки запросов от сервера.
"""

from .get import GetRequests
from .post import PostRequests
from ..common.logger import Logger


class Requests:
    """
    Определяет тип пришедшего запроса и выделяет из него тело запроса

    Также формирует системное сообщение о типе пришедшего запроса и пришедших данных
    """

    @staticmethod
    def parse_server_request_parameters(server_data):
        """
        Определяет тип запроса сервера и разбирает пришедшие данные для дальнейшей обработки
        """

        request = {}
        request_method = server_data['REQUEST_METHOD']
        if request_method == 'POST':
            data = PostRequests().get_request_params(server_data)
            request['post_data'] = data
        if request_method == 'GET':
            data = GetRequests().get_request_params(server_data)
            request['get_request_params'] = data
        Requests.send_result_message(request_method, request, server_data['PATH_INFO'])
        return request

    @staticmethod
    def send_result_message(request_method, request, path):
        """
        Выводит системное сообщение с результатами обработки запроса
        """

        logger = Logger.get_logger()

        str_path = f", по адресу: {path}"
        message = (f'Нам пришёл post-запрос: {request["post_data"]}{str_path}'
                   if request_method == 'POST'
                   else f'Нам пришли GET-параметры: {request["get_request_params"]}{str_path}')

        logger.log(message)
