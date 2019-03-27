from django.db import models
from pasta_family.models import Product


class DayliStatistic(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    new_orders = models.IntegerField(verbose_name='New orders')
    finish_orders = models.IntegerField(verbose_name='Finish orders')
    money = models.IntegerField(verbose_name='Money')


class DayItem(models.Model):
    day = models.ForeignKey(DayliStatistic, related_name='items', on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name='day_statistic_items', on_delete=models.CASCADE,)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Amount', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class MonthStatistic(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    finish_orders = models.IntegerField(verbose_name='Finish orders')
    money = models.IntegerField(verbose_name='Money')


class MonthItem(models.Model):
    month = models.ForeignKey(MonthStatistic, related_name='items', on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name='month_statistic_items', on_delete=models.CASCADE,)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Amount', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

