# Generated by Django 4.2.6 on 2023-10-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_remove_menu_link_menuitem_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='link',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Ссылка для перехода'),
        ),
    ]
