# Generated by Django 2.1.4 on 2019-03-02 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novaposhta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['id'], 'verbose_name': 'Area', 'verbose_name_plural': 'Areas'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['id'], 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'ordering': ['id'], 'verbose_name': 'Warehouse', 'verbose_name_plural': 'Warehouses'},
        ),
    ]
