# Коды ответов сервера
server_answers = {
    '100': 'базовое уведомление',
    '101': 'важное уведомление',
    '200': 'OK',
    '201': '(created): объект создан',
    '202': '(accepted): подтверждение',
    '400': 'неправильный запрос/JSON-объект',
    '401': 'не авторизован',
    '402': 'неправильный логин/пароль',
    '403': '(forbidden): пользователь заблокирован',
    '404': '(not found): пользователь/страница отсутствует на сервере',
    '409': '(conflict): уже имеется подключение с указанным логином',
    '410': '(gone): адресат существует, но недоступен: (offline)',
    '500': 'ошибка сервера',
}

# Методы протокола (actions)
protocol_methods = {
    'action': (
        'presence', 'присутствие. Контроллер запущен'), 'action': (
        'prоbe', 'проверка присутствия. Сервисное сообщение от сервера для проверки '
                 'корректности ответа контроллера'), 'action': (
        'msg', 'простое сервисное сообщение о состоянии контроллера'), 'action': (
        'quit', 'отключение от контроллера'), 'action': (
        'authenticate', 'авторизация пользователя на сервере'), }
