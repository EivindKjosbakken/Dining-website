# Generated by Django 3.1.7 on 2021-03-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_ownuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
