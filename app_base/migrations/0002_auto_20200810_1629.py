# Generated by Django 3.1 on 2020-08-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.PositiveSmallIntegerField(choices=[(1, 'یخچال امرسان'), (2, 'گاز بهمن')], null=True),
        ),
    ]
