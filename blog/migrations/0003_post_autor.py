# Generated by Django 2.2.7 on 2019-12-01 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_post_dt_pub_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
