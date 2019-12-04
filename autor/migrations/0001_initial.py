# Generated by Django 2.2.7 on 2019-12-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField(max_length=2)),
                ('sexo', models.TextField(max_length=10)),
                ('e_mail', models.EmailField(max_length=254)),
                ('resu_perfil', models.CharField(max_length=255)),
            ],
        ),
    ]