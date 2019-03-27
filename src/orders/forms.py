from django import forms
from .models import Order, Delivery, PaymentMethod, OrderStatus


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = '__all__'

