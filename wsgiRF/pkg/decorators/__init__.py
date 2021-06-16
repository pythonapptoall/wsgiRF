"""
Модуль содержит декораторы для связи роутов и ответственных за них приложений
"""

from .middle_ware import MidleWareOn
from .services import AppRoutes, GetRequest, PostRequest, NotFoundRequest
