# Generated by Django 3.1.7 on 2021-03-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210222_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownuser',
            name='city',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
