# Generated by Django 3.0.1 on 2020-01-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupprojects', '0010_auto_20200112_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='is_approve',
            field=models.BooleanField(default=False),
        ),
    ]
