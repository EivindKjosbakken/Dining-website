# Generated by Django 3.1.7 on 2021-03-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinners', '0012_auto_20210315_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='allergies',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
