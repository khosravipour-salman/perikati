# Generated by Django 3.1 on 2020-08-31 13:10

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0004_testmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.PositiveSmallIntegerField(choices=[(1, 'یخچال/فریزر (REF)'), (2, 'اجاق گاز (GC)'), (3, 'ماشین لباسشویی (WM)'), (4, 'تلویزیون (TV)'), (5, 'لوازم خانگی کوچک (SHA)'), (6, 'متفرقه (OTHER)'), (7, 'محصولات نوکار (BI)'), (8, 'ماشین ظرفشویی (DW)'), (9, 'تهویه هوا (AC)')], null=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='date',
            field=django_jalali.db.models.jDateTimeField(),
        ),
    ]
