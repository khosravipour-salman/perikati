# Generated by Django 3.1 on 2020-09-02 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0015_productmodel_factor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='factor',
            new_name='factors',
        ),
    ]
