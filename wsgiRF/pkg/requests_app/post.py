"""
Модуль обрабатывает POST запросы
"""

import quopri

from .request_abc import RequestsABC


class PostRequests(RequestsABC):
    """
    Класс обрабатывает POST запросы и возвращает словарь с данными тела запроса

    Является наследником класса RequestsABC
    """

    @staticmethod
    def get_input_data(server_data) -> bytes:
        """
        Выделяет из данных, пришедших от сервера, тело запроса
        """

        content_length_data = server_data.get('CONTENT_LENGTH')
        int_content_length_data = int(
            content_length_data) if content_length_data else 0
        request_data = server_data['wsgi.input'].read(
            int_content_length_data) if int_content_length_data > 0 else b''
        return request_data

    def parse_input_data(self, request_data: bytes) -> dict:
        """
        Распаковывает тело запроса
        """

        request_decode_value_dic = {}

        if request_data:
            request_decode_value = request_data.decode('UTF-8')
            corrected_request_decode_value = self.get_correct_decode_value(
                request_decode_value)
            request_decode_value_dic = self.parse_into_dic(
                corrected_request_decode_value)
        return request_decode_value_dic

    @staticmethod
    def get_correct_decode_value(request_data_str):
        """
        Модуль quopri выполняет quoted-printable транспортное кодирование и декодирование
        как определено в RFC 1521: «MIME (Многоцелевые расширения почты интернета) часть первая:
        механизмы определения и описания формата сообщений интернета».

        Он исправляет неоднозначности кодирования, в том числе, POST запросов.
        Для корректного декодирования в utf-8 строку запроса вида "%D0%BA" превратит в
        b"=D0=BA", а далее в b"\xd0\xba".
        """

        request_data_str_b = bytes(request_data_str.replace(
            '=', '///').replace('%', '=').replace("+", " "), 'UTF-8')
        request_data_str_b = quopri.decodestring(request_data_str_b)
        return request_data_str_b.decode('UTF-8').replace('///', '=')
