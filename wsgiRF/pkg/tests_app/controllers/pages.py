"""
Данные контроллеры обрабатывают запросы к конкретной странице или выполняют конкретное действие
по запросу
"""

from controllers_app.decorators.page import NotFoundRequest, GetRequest, PostRequest


@GetRequest(route="/")
class IndexPage:
    """ Класс для обработки запросов к главной странице """

    def __call__(self, request):
        return '200 OK', request


@PostRequest(route="/post_request/")
class PostRequest:
    """ Класс для обработки POST запросов """

    def __call__(self, request):
        return '200 OK', request


@NotFoundRequest(route="NotFound")
class NotFound404Page:
    """ Класс для обработки запросов к несуществующей странице """

    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
