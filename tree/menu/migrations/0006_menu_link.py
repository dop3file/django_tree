# Generated by Django 4.2.6 on 2023-10-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='link',
            field=models.CharField(max_length=512, null=True, verbose_name='Ссылка для перехода'),
        ),
    ]
