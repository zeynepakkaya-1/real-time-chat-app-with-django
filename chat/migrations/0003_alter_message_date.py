# Generated by Django 4.1.7 on 2023-02-21 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_roomname_message_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 21, 10, 38, 45, 23678, tzinfo=datetime.timezone.utc)),
        ),
    ]
