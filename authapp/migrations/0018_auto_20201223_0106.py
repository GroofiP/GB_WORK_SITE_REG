# Generated by Django 3.1.3 on 2020-12-23 01:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0017_auto_20201222_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 1, 6, 41, 264430, tzinfo=utc)),
        ),
    ]