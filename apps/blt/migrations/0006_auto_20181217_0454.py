# Generated by Django 2.1.4 on 2018-12-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blt', '0005_auto_20181217_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='aid',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tid',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
