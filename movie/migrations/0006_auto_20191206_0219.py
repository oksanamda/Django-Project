# Generated by Django 3.0 on 2019-12-05 23:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20191206_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)]),
        ),
        migrations.AlterField(
            model_name='moviedirector',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
