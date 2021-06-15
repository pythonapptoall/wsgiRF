"""
Содержит дебагер для отслеживания параметров работы методов или классов проекта
"""

import time


class Debug:
    """
    Работает как декоратор. Имеет возможность принимать параметры на входе!

    На данном этапе реализована возможность получать методы,
    которые выполняются дольше, чем заданное в декораторе время в секундах.

    Запускается:
        @Debug(critical_time=3, name='любое имя для идентификации')

    """

    def __init__(self, critical_time, name):
        """
        Сохраняем значение переданных параметров при инициализации экземпляра
        """

        self.critical_time = critical_time
        self.name = name

    def __call__(self, cls):
        """
        При вызове декоратора
        """

        def timeit(method):
            """
            Сама функция-декоратор
            """

            def timed(*args, **kwargs):
                """
                Засекает время начала выполнения метода и время окончания его выполнения.

                Рассчитывает время работы метода в секундах и выводит сообщение, если
                время превысило заданную величину
                """

                start_time = time.time()
                result = method(*args, **kwargs)
                end_time = time.time()
                delta_in_seconds = (end_time - start_time) * 1000
                if delta_in_seconds > self.critical_time:
                    print(
                        f'debug --> {self.name} выполнялся {delta_in_seconds:2.2f} '
                        f'сек., это дольше заданных {self.critical_time} сек.')
                return result

            return timed

        return timeit(cls)
