# Generated by Django 3.1 on 2020-08-31 13:16

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0005_auto_20200831_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='date',
            field=django_jalali.db.models.jDateField(),
        ),
    ]
