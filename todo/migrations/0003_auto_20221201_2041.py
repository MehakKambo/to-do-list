# Generated by Django 3.0.6 on 2022-12-01 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20221130_0719'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to=None,
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
