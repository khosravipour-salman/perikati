# Generated by Django 3.1 on 2020-08-31 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0009_factormodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factormodel',
            options={'ordering': ('-datetime',), 'verbose_name_plural': 'پیش فاکتور ها'},
        ),
        migrations.RenameField(
            model_name='factormodel',
            old_name='customer_extra_explanation',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='factormodel',
            name='customer_birth',
        ),
        migrations.AddField(
            model_name='factormodel',
            name='customer_birthdate',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='factormodel',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='factors', to='app_base.productmodel'),
        ),
    ]
