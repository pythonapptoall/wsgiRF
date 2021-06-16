"""
Данные контроллеры стоят между фреймворком и Контроллерами страниц (pages).
Обрабатывают общие вопросы для всех страниц: проверка безопасности, проверка разрешения на
доступ пользователей к различным ресурсам или изменения параметров запроса с учетом вида спорта.
Если не централизовать выполнение этих или похожих функций, то это приведёт к дублированию
большой части кода.
"""

from datetime import date

from controllers_app.decorators.front import FrontOn


@FrontOn()
def front_controller_set_current_date(request):
    """ Передает на страницы текущую дату """

    request['date'] = date.today()
    return request


@FrontOn()
def front_controller_set_secret_key(request):
    """ Просто образец, передает любую служебную информацию на страницы """

    request['secret_key'] = 'something'
    return request
