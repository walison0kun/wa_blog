# Generated by Django 2.2.7 on 2019-12-05 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_auto_20191204_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='idade',
            field=models.CharField(max_length=2),
        ),
    ]
