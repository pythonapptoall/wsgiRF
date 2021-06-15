"""
Если надо вернуть ответ в виде html страницы из шаблона.

Создает страницу на основе шаблона и пришедших данных.

Используем шаблонизатор jinja2
"""
import os
from jinja2 import Template


def render(template_name, templates_folder='templates', **kwargs):
    """
    Рендер из шаблона
    :param template_name: имя шаблона
    :param templates_folder: путь, где хранится шаблон
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    page_file_path = os.path.join(templates_folder, template_name)
    with open(page_file_path, encoding='utf-8') as page_body_file:
        template = Template(page_body_file.read())
    return template.render(**kwargs)
