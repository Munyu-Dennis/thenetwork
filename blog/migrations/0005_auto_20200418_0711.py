# Generated by Django 3.0 on 2020-04-18 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='titlee',
            new_name='title',
        ),
    ]
