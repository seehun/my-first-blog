# Generated by Django 4.2.6 on 2023-10-09 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 9, 16, 36, 5, 946829, tzinfo=datetime.timezone.utc)),
        ),
    ]
