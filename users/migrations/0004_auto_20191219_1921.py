# Generated by Django 2.2.8 on 2019-12-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191219_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='code',
            field=models.CharField(default='000000', max_length=6),
        ),
    ]
