# Generated by Django 4.1 on 2022-09-28 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_task_finish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='finish',
            new_name='is_finished',
        ),
    ]
