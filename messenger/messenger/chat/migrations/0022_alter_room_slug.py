# Generated by Django 4.0.4 on 2022-05-24 19:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0021_alter_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]
