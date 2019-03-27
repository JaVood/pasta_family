from orders.models import Order, OrderItem
from .models import DayItem, DayliStatistic, MonthStatistic, MonthItem
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import date


@periodic_task(
    run_every=(crontab(minute=0, hour='23')),
    name="daylistatistic",
    ignore_result=True
)
def daylistatistic():
    day = date.today()
    orders = Order.objects.filter(created__date=date.today())
    updated = Order.objects.filter(updated__date=date.today())
    new = 0
    money = 0
    finish = 0
    day_name = '{}.{}.{}'.format(day.day, day.month, day.year)
    day = DayliStatistic.objects.create(name=day_name, new_orders=new, finish_orders=finish, money=money)
    for i in orders:
        new += 1
    for i in updated:
        items = OrderItem.objects.filter(order_id=i.id)
        if i.order_status_id == 2:
            finish += 1
        for j in items:
            if i.order_status_id == 2:
                DayItem.objects.create(day=day, product_id=j.product_id, price=j.product.price, quantity=j.quantity)
                money += j.product.price * j.quantity
    day.new_orders = new
    day.finish_orders = finish
    day.money = money
    day.save()


@periodic_task(
    run_every=(crontab(0, 0, day_of_month='1')),
    name="monthlistatistic",
    ignore_result=True
)
def monthlistatistic():
    month = date.today()
    month = month.month - 1
    updated = Order.objects.filter(updated__month=month)
    money = 0
    finish = 0
    month_name = 'no orders'
    day = date.today()
    month = MonthStatistic.objects.create(name=month_name, finish_orders=finish, money=money)
    for i in updated:
        month_name = '{}.{}.{}'.format(day.day, i.updated.month, i.updated.year)
        items = OrderItem.objects.filter(order_id=i.id)
        if i.order_status_id == 2:
            finish += 1
        for j in items:
            if i.order_status_id == 2:
                MonthItem.objects.create(month=month, product_id=j.product_id, price=j.product.price, quantity=j.quantity)
                money += j.product.price * j.quantity
    month.name = month_name
    month.finish_orders = finish
    month.money = money
    month.save()
