# Generated by Django 4.2.7 on 2023-11-11 09:59

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]