# Generated by Django 4.0.4 on 2022-05-18 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='chat',
        ),
        migrations.DeleteModel(
            name='messege',
        ),
    ]
