# Generated by Django 2.1.4 on 2019-03-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='warehouse',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Warehouse'),
        ),
    ]
