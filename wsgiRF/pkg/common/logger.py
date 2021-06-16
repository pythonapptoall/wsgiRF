"""
Логгер, выводит информацию о работе программы.

Пока в консоль. При необходимости можно в базу или файл. Меняется только последняя строчка
логгера
"""


class SingletonByName(type):
    """
    Родительский класс логгера.

    Является синглтоном, то есть на время работы создается только один экземпляр
    данного класса и данный экземпляр будет доступен из любого места программы
    """

    def __init__(cls, name, bases, attrs):
        """
        Инициируем свой класс из стандартного класса type
        """

        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        """
        При вызове класса проверяем существование экземпляра с таким именем,
        если существует, то просто возвратим существующий вместо создания нового
        """

        name = ''

        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]

        cls.__instance[name] = super().__call__(*args, **kwargs)
        return cls.__instance[name]


class Logger(metaclass=SingletonByName):
    """
    Собственно логгер

    При инициализации сохраняет имя, по которому будет доступен. При вызове выводит
    заданное сообщение в консоль.

    Инициализируется и повторно вызывается командой: logger = Logger.get_logger()
    Отправка сообщения: logger.log('text')
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def start_logger(name):
        """
        Возвращает ссылку на запущенный логгер или запускает его, если не был запущен
        """

        return Logger(name)

    @staticmethod
    def get_logger(name):
        """
        Возвращает ссылку на запущенный логгер или запускает его, если не был запущен
        """

        return Logger(name)

    @staticmethod
    def log(text):
        """
        Выводит сообщение в терминал
        """

        print('log--->', text)
