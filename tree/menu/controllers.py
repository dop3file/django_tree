from .models import MenuItem, Menu


def get_menu(title: str) -> Menu:
    return Menu.objects.filter(title=title).first()


def get_menu_items(menu: Menu) -> list[MenuItem]:
    menu_items = menu.items.order_by("parent__id").all()

    return menu_items


def _group_dfs(groups: dict, item: MenuItem):
    tmp_item = item
    parents = []
    while tmp_item.parent:
        parents.append(tmp_item.parent)
        tmp_item = tmp_item.parent
    tmp_groups = groups
    for parent in parents[::-1]:
        tmp_groups = tmp_groups[parent]
    tmp_groups[item] = {}


def group_menu_items(items: list[MenuItem]) -> dict:
    groups = {}
    for item in items:
        _group_dfs(groups, item)
    return groups