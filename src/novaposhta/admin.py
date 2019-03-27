from importlib import import_module

from django.apps import apps
from django.contrib import admin

from .models import Warehouse, Area, City


def _get_warehouse_admin_base_class():

    if apps.is_installed('modeltranslation'):
        return import_module('modeltranslation.admin').TranslationAdmin

    return admin.ModelAdmin


class WarehouseAdmin(_get_warehouse_admin_base_class()):

    list_display = ['title', 'address', 'city']
    search_fields = ['title', 'address', 'city']


admin.site.register(Warehouse, WarehouseAdmin)


class AreaAdmin(_get_warehouse_admin_base_class()):

    list_display = ['area', 'ref']
    search_fields = ['area', 'ref']


admin.site.register(Area, AreaAdmin)


class CityAdmin(_get_warehouse_admin_base_class()):

    list_display = ['area', 'city', 'area']
    search_fields = ['area', 'city', 'area']


admin.site.register(City, CityAdmin)
