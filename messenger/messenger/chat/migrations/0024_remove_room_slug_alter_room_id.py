# Generated by Django 4.0.4 on 2022-05-24 19:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0023_alter_room_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
