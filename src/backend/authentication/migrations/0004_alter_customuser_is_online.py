# Generated by Django 4.0.6 on 2022-07-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_customuser_is_banned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]