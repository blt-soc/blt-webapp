# Generated by Django 2.1.4 on 2018-12-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blt', '0008_auto_20181217_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='value',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
    ]
