# Generated by Django 2.0.2 on 2018-02-19 15:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0021_classes_could_be_blank'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clazz',
            new_name='Class',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='clazzes',
            new_name='classes',
        ),
    ]
