from django.db import models
from pasta_family.models import Product
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from novaposhta.models import Area, Warehouse, City
from smart_selects.db_fields import ChainedForeignKey
from .tasks import OrderSend


class Order(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    address = models.CharField(verbose_name='Adress', max_length=250, blank=True)
    postal_code = models.CharField(verbose_name='ZIP Code', max_length=20, blank=True)
    city = models.CharField(verbose_name='City', max_length=100, blank=True)
    created = models.DateTimeField(verbose_name='Create', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Update', auto_now=True)
    paid = models.BooleanField(verbose_name='Paid', default=False)
    paid_status = models.CharField(verbose_name='paid_status', max_length=50, blank=True)
    message = models.CharField(verbose_name='Message', max_length=250, blank=True)
    declaration = models.CharField(verbose_name='Declaration', max_length=250, blank=True)
    call_back = models.BooleanField(verbose_name='No Call Back', default=False)

    order_status = models.ForeignKey(
        to='OrderStatus',
        on_delete=models.PROTECT,
        verbose_name=_('Order Status'),
        blank=True,
        null=True
    )

    payment_method = models.ForeignKey(
        to='PaymentMethod',
        on_delete=models.PROTECT,
        verbose_name=_('Payment Method'),
    )
    delivery = models.ForeignKey(
        to='Delivery',
        on_delete=models.PROTECT,
        verbose_name=_('Delivery'),
    )

    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        verbose_name=_('Area'),
        blank=True,
        null=True,
    )

    nova_city = ChainedForeignKey(
        City,
        chained_field="area",
        chained_model_field="area_id",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name=_('Nova Poshta City'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    nova_warehouse = ChainedForeignKey(
        Warehouse,
        chained_field="nova_city",
        chained_model_field="city_id",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name=_('Nova Poshta Warehouse'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    warehouse = models.CharField(verbose_name='Warehouse', max_length=3000, blank=True, null=True)
    class Meta:
        ordering = ('-created', )
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order: {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost

    def save(self, *args, **kwargs):
        if self.paid_status == 'sandbox' or self.paid_status == 'success' or self.paid_status == 'wait_accept':
            self.paid = True
        if self.order_status == None:
            self.order_status = OrderStatus.objects.get(id=1)
        super(Order, self).save(*args, **kwargs)
        if self.declaration:
            OrderSend(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT,)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Amount', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Delivery(models.Model):
    name_ru = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Delivery In Russian'),
    )

    name_en = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Delivery In English'),
    )

    name_ua = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Delivery In Ukraine'),
    )

    def __str__(self):
        return self.name_ru


class PaymentMethod(models.Model):
    name_ru = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Payment Method In Russian'),
    )

    name_en = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Payment Method In English'),
    )

    name_ua = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Payment Method In Ukraine'),
    )

    def __str__(self):
        return self.name_ru


class OrderStatus(models.Model):
    name_ru = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Order Status In Russian'),
    )

    name_en = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Order Status In English'),
    )

    name_ua = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Order Status In Ukraine'),
    )

    def __str__(self):
        return self.name_ru

