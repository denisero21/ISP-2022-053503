# Generated by Django 4.0.4 on 2022-05-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0003_auth_register_remove_post_author_delete_messege_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='auth',
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]