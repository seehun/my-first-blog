# Generated by Django 4.2.6 on 2023-10-09 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 9, 16, 25, 22, 776701, tzinfo=datetime.timezone.utc)),
        ),
    ]
