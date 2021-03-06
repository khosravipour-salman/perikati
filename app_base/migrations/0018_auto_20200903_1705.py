# Generated by Django 3.1 on 2020-09-03 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0017_auto_20200903_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factormodel',
            name='customer_city',
            field=models.CharField(max_length=20, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='factormodel',
            name='customer_last_name',
            field=models.CharField(max_length=80, verbose_name='نام خانوادگی خریدار'),
        ),
        migrations.AlterField(
            model_name='factormodel',
            name='customer_name',
            field=models.CharField(max_length=20, verbose_name='نام خریدار'),
        ),
        migrations.AlterField(
            model_name='factormodel',
            name='customer_national_code',
            field=models.CharField(max_length=10, verbose_name='کد ملی خریدار'),
        ),
        migrations.AlterField(
            model_name='factormodel',
            name='customer_phone_number',
            field=models.CharField(max_length=12, verbose_name='شماره همراه خریدار'),
        ),
        migrations.AlterField(
            model_name='factormodel',
            name='customer_postal_code',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')], verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='factormodel',
            name='customer_state',
            field=models.CharField(max_length=20, verbose_name='استان'),
        ),
    ]
