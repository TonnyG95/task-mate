# Generated by Django 3.2.13 on 2022-06-14 05:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_tasklist_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
