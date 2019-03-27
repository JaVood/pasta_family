"""pasta_family URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('boss/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    re_path(r'', include(('pasta_family.urls', 'pasta_family'), namespace='pasta_family')),
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^order/', include(('orders.urls', 'orders'), namespace='orders')),
    path('novaposhta/', include('novaposhta.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
