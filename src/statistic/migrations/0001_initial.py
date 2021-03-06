# Generated by Django 2.1.4 on 2018-12-17 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pasta_family', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='DayliStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('new_orders', models.IntegerField(verbose_name='New orders')),
                ('finish_orders', models.IntegerField(verbose_name='Finish orders')),
                ('money', models.IntegerField(verbose_name='Money')),
            ],
        ),
        migrations.CreateModel(
            name='MonthItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='MonthStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('finish_orders', models.IntegerField(verbose_name='Finish orders')),
                ('money', models.IntegerField(verbose_name='Money')),
            ],
        ),
        migrations.AddField(
            model_name='monthitem',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='statistic.MonthStatistic'),
        ),
        migrations.AddField(
            model_name='monthitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='month_statistic_items', to='pasta_family.Product'),
        ),
        migrations.AddField(
            model_name='dayitem',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='statistic.DayliStatistic'),
        ),
        migrations.AddField(
            model_name='dayitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_statistic_items', to='pasta_family.Product'),
        ),
    ]
