"""
Модуль содержит декораторы для формирования списка используемых front контроллеров
"""


class MidleWareOn:
    """
    Используется как декоратор midleware, которое должны использоваться.
    Пример использования:
        @MidleWareOn()
    Формирует список midlewares, содержащий ссылки на классы используемых midleware:
         [
                midleware_set_current_date,
                midleware_set_secret_key,
         ]
    Через @classmethod собирает список со всех экземпляров класса MidleWareOn в один список,
    методы класса позволяют работать с ним через имя класса, не вызывая его экземпляров:
        MidleWareOn.get_front_controllers_list()
    """

    midlewares = []

    def __call__(self, cls):
        """
        Вызов декоратора.

        Добавляем вызвавший метод в список для применения
        """

        MidleWareOn.midlewares += [cls]

    @classmethod
    def get_middleware_list(cls):
        """
        Вернет список доступных фронт контроллеров
        """

        return cls.midlewares
