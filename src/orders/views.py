from django.shortcuts import get_object_or_404
from .models import OrderItem, Order, Delivery, PaymentMethod
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from novaposhta.models import Area
from .tasks import OrderCreated
from .liqpay import LiqPay
from django.shortcuts import render
from django.http import HttpResponse
from core import settings
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



@staff_member_required
def AdminOrderPDF(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf'.format(order.id)
    # weasyprint.HTML(string=html).write_pdf(response,
    #            stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/bootstrap.min.css')])
    return response


@staff_member_required
def AdminOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})


def OrderCreate(request):
    cart = Cart(request)
    deliveries = Delivery.objects.all()
    payments = PaymentMethod.objects.all().order_by('id')
    area_list = Area.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.warehouse = order.nova_warehouse
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            OrderCreated.delay(order.id)
            return form_send(request, order=order)
    form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form,
                                                        'deliveries': deliveries,
                                                        'payments': payments,
                                                        'areas': area_list,
                                                        })


def form_send(request, order):
    cart = Cart(request)
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    a = OrderItem.objects.filter(order_id=order)
    price = 0
    for i in a:
        price += i.quantity * i.price
    price = (price * 103) / 100
    params = {
        'action': 'pay',
        'amount': float(price),
        'currency': 'UAH',
        'description': order.id,
        'order_id': order.id,
        'version': '3',
        'server_url': 'http://pasta-family.com.ua/order/pay-callback/',
        'language': 'ua',
    }
    signature = liqpay.cnb_signature(params)
    data = liqpay.cnb_data(params)
    return render(request, 'orders/order/form_send.html', {'signature': signature,
                                                           'data': data,
                                                           'cart': cart,
                                                           'order': order})


def form_send_ru(request, order):
    cart = Cart(request)
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    a = OrderItem.objects.filter(order_id=order)
    price = 0
    for i in a:
        price += i.quantity * i.price
    price = (price * 103) / 100
    params = {
        'action': 'pay',
        'amount': float(price),
        'currency': 'UAH',
        'description': order.id,
        'order_id': order.id,
        'version': '3',
        'server_url': 'http://pasta-family.com.ua/order/pay-callback/',
        'language': 'ru',
    }
    signature = liqpay.cnb_signature(params)
    data = liqpay.cnb_data(params)
    return render(request, 'orders/order/form_send_ru.html', {'signature': signature,
                                                              'data': data,
                                                              'cart': cart,
                                                              'order': order})


def OrderCreateRu(request):
    cart = Cart(request)
    deliveries = Delivery.objects.all()
    payments = PaymentMethod.objects.all().order_by('id')
    area_list = Area.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.warehouse = order.nova_warehouse
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            OrderCreated.delay(order.id)
            return form_send_ru(request, order=order)
    form = OrderCreateForm()

    return render(request, 'orders/order/create_ru.html', {'cart': cart,
                                                           'form': form,
                                                           'deliveries': deliveries,
                                                           'payments': payments,
                                                           'areas': area_list,
                                                           })


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        order_id = response['order_id']
        status = response['status']
        order = Order.objects.get(id=order_id)
        order.paid_status = status
        order.save()
        return HttpResponse()
