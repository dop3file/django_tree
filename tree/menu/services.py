from django.db.models import QuerySet

from .models import MenuItem, Menu


class Crud:
    @staticmethod
    def get_menu_items(title: str) -> QuerySet[MenuItem]:
        menu_items = MenuItem.objects.filter(menu__title=title).order_by("parent__id").all()

        return menu_items


class Services:
    @staticmethod
    def _group_dfs(groups: dict, item: MenuItem, items: list[MenuItem]):
        tmp_item = item
        parents = []
        while tmp_item.parent:
            parents.append(tmp_item.parent)
            tmp_item = tmp_item.parent
        tmp_groups = groups
        for parent in parents[::-1]:
            if parent not in tmp_groups:
                return items.append(item)
            tmp_groups = tmp_groups[parent]
        tmp_groups[item] = {}

    @staticmethod
    def group_menu_items(items: list[MenuItem]) -> dict:
        groups = {}
        print(items)
        for item in items:
            Services._group_dfs(groups, item, items)
        return groups