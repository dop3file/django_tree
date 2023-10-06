from django import template
from django.template.loader import render_to_string

from menu.controllers import get_menu_items, group_menu_items, get_menu


register = template.Library()


@register.simple_tag
def draw_menu(title: str):
    menu = get_menu(title)
    context = {
        "menu": menu,
        "menu_items": group_menu_items(
            get_menu_items(menu)
        )
    }
    template = "menu.html"
    rendered_template = render_to_string(template, context)
    return rendered_template