"""
Модуль настроек:

'LOGGER_NAME'. Имя, под которым запустится логгер приложения

'D_BASE'. Настройки для подключения базы данных

'ADDRESS'. Хост и порт, по которым доступен наш проект. Если Хост пустой, то запускаемся
на localhost:PORT
"""

SETTINGS = {
    'ADDRESS': {
        'HOST': '',
        'PORT': 8080,
    },

    'D_BASE': {
        'user': "costa",
        'password': "costacoffe",
        'host': "localhost",
        'port': "5433",
        'database': "basket2016"
    },

    'LOGGER_NAME': 'main',

}
