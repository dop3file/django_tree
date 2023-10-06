from django.db import models


class MenuItem(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name="Пункт меню"
    )
    parent = models.ForeignKey("self", null=True, blank=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Menu(models.Model):
    title = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name="Названия меню"
    )
    items = models.ManyToManyField(MenuItem)
    link = models.CharField(
        max_length=512,
        null=True,
        verbose_name="Ссылка для перехода"
    )

    def __str__(self):
        return f"{self.title}"