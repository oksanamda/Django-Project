# Generated by Django 3.0 on 2019-12-05 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20191206_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedirector',
            old_name='name',
            new_name='dir_name',
        ),
    ]
