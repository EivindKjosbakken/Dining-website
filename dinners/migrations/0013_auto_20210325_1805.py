# Generated by Django 3.1.6 on 2021-03-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinners', '0012_dinner_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='cost',
            field=models.IntegerField(default=100),
        ),
    ]
