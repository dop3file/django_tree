# Generated by Django 4.2.6 on 2023-10-06 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_menuitem_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='items',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
            preserve_default=False,
        ),
    ]
