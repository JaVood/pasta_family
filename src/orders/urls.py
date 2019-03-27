from django.conf.urls import url, include
from . import views
from orders.views import PayCallbackView

urlpatterns = [
    url(r'^create/$', views.OrderCreate, name='OrderCreate'),
    url(r'^create/ru/$', views.OrderCreateRu, name='OrderCreateRu'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.AdminOrderDetail, name='AdminOrderDetail'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.AdminOrderPDF, name='AdminOrderPDF'),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^form_send/$', views.form_send, name='form_send'),
    url(r'^ru/form_send/$', views.form_send_ru, name='form_send_ru'),
    url(r'^pay-callback/$', PayCallbackView.as_view(), name='pay_callback'),
]
