from django.urls import re_path
from django.conf.urls import url
import django.views.defaults
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^ofert/$', views.OfertView.as_view(), name='ofert'),
    re_path(r'^ru/ofert/$', views.OfertRuView.as_view(), name='ofert ru'),
    re_path(r'^ru/return/$', views.ReturnRuView.as_view(), name='return ru'),
    re_path(r'^return/$', views.ReturnView.as_view(), name='return'),
    re_path(r'^for_sportmens/$', views.SportView.as_view(), name='sport'),
    re_path(r'^contacts/$', views.ContactView.as_view(), name='contact'),
    re_path(r'^delivery/$', views.DeliveryView.as_view(), name='delivery'),
    url(r'^cooperation/$', views.cooperation_new, name='cooperation'),
    re_path(r'^product_group/$', views.product_group, name='product_group'),
    re_path(r"^product_group/(?P<productgroup_slug>.+[\w-]+[']*)/(?P<product_slug>.+[\w-]+[']*)/$",
            views.ProductView.as_view(), name='product'),
    url(r'^review/$', views.review_new, name='review'),
    re_path(r'^form_send/$', views.FormSendView.as_view(), name='form_send'),
    re_path(r"^product_group/(?P<productgroup_slug>.[\w-]+[']*)/$", views.ProductsView.as_view(), name='products'),

    re_path(r'^ru/$', views.IndexRuView.as_view(), name='index'),
    re_path(r'^ru/about/$', views.AboutRuView.as_view(), name='about'),
    re_path(r'^ru/for_sportmens/$', views.SportRuView.as_view(), name='sport'),
    re_path(r'^ru/contacts/$', views.ContactRuView.as_view(), name='contact'),
    re_path(r'^ru/delivery/$', views.DeliveryRuView.as_view(), name='delivery'),
    url(r'^ru/cooperation/$', views.cooperation_new_ru, name='cooperation'),
    re_path(r'ru/product_group/$', views.product_group_ru, name='product_group'),
    re_path(r"^ru/product_group/(?P<productgroup_slug>.+[\w-]+[']*)/(?P<product_slug>.+[\w-]+[']*)/$",
            views.ProductRuView.as_view(), name='product'),
    url(r'^ru/review/$', views.review_new_ru, name='review'),
    re_path(r'^ru/form_send/$', views.FormSendRuView.as_view(), name='form_send'),
    re_path(r"^ru/product_group/(?P<productgroup_slug>[\w-]+[']*)/$", views.ProductsRuView.as_view(), name='products'),
    url(r'^404/$', django.views.defaults.page_not_found, ),
    url(r'^order_check/$', views.order_check, name='order_check'),
    url(r'^order_details/$', views.order_detail, name='order_detail'),
    url(r'^ru/order_check/$', views.order_check_ru, name='order_check'),
    url(r'^ru/order_details/$', views.order_detail_ru, name='order_detail'),
]
