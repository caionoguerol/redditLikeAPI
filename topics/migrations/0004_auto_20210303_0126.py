# Generated by Django 3.0.7 on 2021-03-03 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20210303_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='user_profile',
            new_name='author',
        ),
    ]