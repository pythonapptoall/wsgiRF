"""
Модуль содержит декораторы для формирования списка используемых front контроллеров
"""


class FrontOn:
    """
    Используется как декоратор front контроллеров, которые должны использоваться.
    Пример использования:
        @FrontOn()
    Формирует список fronts, содержащий ссылки на классы используемых front контроллеров:
         [
                front_controller_set_current_date,
                front_controller_set_secret_key,
         ]
    Через @classmethod собирает список со всех экземпляров класса FrontOn в один список,
    методы класса позволяют работать с ним через имя класса, не вызывая его экземпляров:
        FrontOn.get_front_controllers_list()
    """

    fronts = []

    def __call__(self, cls):
        """
        Вызов декоратора.

        Добавляем вызвавший метод в список для применения
        """

        FrontOn.fronts += [cls]

    @classmethod
    def get_front_controllers_list(cls):
        """
        Вернет список доступных фронт контроллеров
        """

        return cls.fronts
