# Generated by Django 3.1.7 on 2021-03-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinners', '0006_merge_20210311_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='category',
            field=models.CharField(default='other', max_length=50),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='date',
            field=models.CharField(default='10.02.2021', max_length=10),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='time',
            field=models.CharField(default='16.00', max_length=10),
        ),
    ]
