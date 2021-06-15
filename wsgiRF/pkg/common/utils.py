"""
Модуль для хранения утилит
"""

import sys
import datetime
import json

class Utils:
    """
    Класс содержит короткие утилиты, которые могут быть использованы во всех модулях
    """

    @staticmethod
    def to_unit_dictionaries_in_one_dictionary(*args):
        """
        Небольшая утилита для объединения нескольких словарей в один
        """
        data = {}
        for dic in args:
            data = {**data, **dic}
        return data

    @staticmethod
    def set_project_modules_relative_import_paths():
        """
        Добавляет возможность импортировать модули внутри проекта по относительному пути
        от корневого модуля

        sys.path[0] ссылается на путь, из которого был запущен проект.
        """

        sys.path.append(sys.path[0] + "/..")
        sys.path.append(sys.path[0] + "/.")


class Json:
    """
     Решение для рекурсивного кодирования и декодирования не поддерживаемых по умолчанию объектов
     datetime.datetime и datetime.date с использованием стандартного модуля библиотеки json.

     Для взаимодействия со строками даты ISO из других источников, которые могут включать
     имя часового пояса или смещение UTC, может потребоваться удалить некоторые части строки
     даты перед преобразованием.

     Декодирование работает только тогда, когда строки даты ISO являются значениями строка
     в JavaScript или во вложенных строковых структурах внутри объекта.
     ISO дата строки, являющиеся элементами массива верхнего уровня, декодироваться не будут.
    """

    class JSONDateTimeEncoder(json.JSONEncoder):
        """
        Используется при кодировании объектов Python в json заменяя собой стандартный метод.

        Используя json и его подкласс JSONEncoder переопределяет метод default(),
        чтобы предоставить свои собственные, пользовательские, сериализаторы.
        """

        def default(self, obj):
            """
            Cериализует объект Python datetime в JSON как строку ISO 8601 datetime:
            obj.isoformat()
            """

            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

            return json.JSONEncoder.default(self, obj)

    @staticmethod
    def datetime_decoder(data):
        """
        Функция используется при десериализации json, заменяет собой стандартный
        декодировщик.

        Подставляется в loads->object_hook и будет вызываться с результатом декодирования каждого
        объекта JSON, и его возвращаемое значение будет использоваться вместо полученного dict.

        Умеет декодировать в Python datetime.
        """

        pairs = {}

        if isinstance(data, list):
            pairs = enumerate(data)
        elif isinstance(data, dict):
            pairs = data.items()
        result = []
        for key, value in pairs:
            if isinstance(value, str):
                try:
                    value = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    try:
                        value = datetime.datetime.strptime(
                            value, '%Y-%m-%d').date()
                    except ValueError:
                        pass
            elif isinstance(value, (dict, list)):
                value = Json.datetime_decoder(value)
            result.append((key, value))
        if isinstance(data, list):
            return [x[1] for x in result]
        elif isinstance(data, dict):
            return dict(result)

    @staticmethod
    def dumps_into_json(obj):
        """
        Кодирует объект Python в json формат
        """
        return json.dumps(obj, cls=Json.JSONDateTimeEncoder)

    @staticmethod
    def loads_from_json(obj):
        """
        Декодирует объект json в Python
        """
        return json.loads(obj, object_hook=Json.datetime_decoder)
