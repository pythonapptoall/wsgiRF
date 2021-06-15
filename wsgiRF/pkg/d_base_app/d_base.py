"""
Модуль работы с базой данных
"""

from contextlib import contextmanager
from copy import copy

import psycopg2
from psycopg2 import Error

from ..common.logger import Logger
from ..common.settings import SETTINGS

D_BASE_SETTINGS = copy(SETTINGS)
LOGGER = Logger.get_logger()
D_BASE_CONNECTION_SETTINGS = D_BASE_SETTINGS['D_BASE']


def get_connection_info(connection):
    """ Возвращает параметры подключения к базе данных """
    return connection.get_dsn_parameters()


@contextmanager
def open_db_connection(commit=False):
    """
    Оборачиваем соединение с базой данных в контекстный менеджер

    Использование:
    with open_db_connection() as cursor:
        наш код
    """

    connection = psycopg2.connect(**D_BASE_CONNECTION_SETTINGS)
    cursor = connection.cursor()
    LOGGER.log(
        f'Информация о сервере PostgreSQL:{get_connection_info(connection)}')

    try:
        yield cursor
    except (Exception, Error) as err:
        LOGGER.log("Ошибка при работе с PostgreSQL:", err)
    else:
        if commit:
            cursor.execute("COMMIT")
        else:
            cursor.execute("ROLLBACK")
    finally:
        if connection:
            cursor.close()
            connection.close()
            LOGGER.log("Соединение с PostgreSQL закрыто")
