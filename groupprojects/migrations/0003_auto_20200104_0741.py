# Generated by Django 3.0.1 on 2020-01-04 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupprojects', '0002_project_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='status',
            new_name='completed_status',
        ),
    ]
