# Generated by Django 3.1.6 on 2021-02-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='vei', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='allergies',
            field=models.TextField(default='gluten'),
        ),
    ]
