# Generated by Django 2.1 on 2019-07-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrs', '0003_auto_20190722_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='company_id',
            field=models.CharField(default='', max_length=12),
        ),
    ]
