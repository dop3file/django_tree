from django import template
from django.template.loader import render_to_string

from menu.services import Services, Crud


register = template.Library()


@register.simple_tag
def draw_menu(title: str):
    context = {
        "title": title,
        "menu_items": Services.group_menu_items(
            list(Crud.get_menu_items(title))
        )
    }
    template = "menu.html"
    rendered_template = render_to_string(template, context)
    return rendered_template