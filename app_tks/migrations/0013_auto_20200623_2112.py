# Generated by Django 3.0.7 on 2020-06-23 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tks', '0012_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='Link',
        ),
    ]
