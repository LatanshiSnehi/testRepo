# Generated by Django 2.1 on 2019-07-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrs', '0007_auto_20190724_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Userid', models.IntegerField(default=10)),
                ('Resume_file', models.FileField(null=True, upload_to='Documents')),
            ],
        ),
    ]
