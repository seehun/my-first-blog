# Generated by Django 4.2.6 on 2023-10-09 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 9, 15, 11, 26, 211317, tzinfo=datetime.timezone.utc)),
        ),
    ]