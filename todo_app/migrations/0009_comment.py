# Generated by Django 3.2.13 on 2022-06-16 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0008_alter_tasklist_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='todo_app.tasklist')),
            ],
        ),
    ]
