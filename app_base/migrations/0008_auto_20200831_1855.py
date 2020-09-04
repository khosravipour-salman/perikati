# Generated by Django 3.1 on 2020-08-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0007_auto_20200831_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[(1, 'یخچال/فریزر (REF)'), (2, 'اجاق گاز (GC)'), (3, 'ماشین لباسشویی (WM)'), (4, 'تلویزیون (TV)'), (5, 'لوازم خانگی کوچک (SHA)'), (6, 'متفرقه (OTHER)'), (7, 'محصولات نوکار (BI)'), (8, 'ماشین ظرفشویی (DW)'), (9, 'تهویه هوا (AC)')], max_length=100)),
                ('number', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='product_title',
        ),
    ]