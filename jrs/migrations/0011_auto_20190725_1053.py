# Generated by Django 2.1 on 2019-07-25 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jrs', '0010_apply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='User_id',
            new_name='Userid',
        ),
    ]
