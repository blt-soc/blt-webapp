# Generated by Django 2.1.4 on 2018-12-17 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blt', '0006_auto_20181217_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='aid',
            field=models.TextField(db_index=True, unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tid',
            field=models.TextField(db_index=True),
        ),
    ]
