from django.contrib import admin
from .models import DayItem, DayliStatistic, MonthItem, MonthStatistic


class DayItemInline(admin.TabularInline):
    model = DayItem
    raw_id_field = ['product']


class DayliStatisticAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'new_orders', 'finish_orders', 'money']
    inlines = [DayItemInline]


class MonthItemInline(admin.TabularInline):
    model = MonthItem
    raw_id_field = ['product']


class MonthStatisticAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'finish_orders', 'money']
    inlines = [MonthItemInline]


admin.site.register(DayliStatistic, DayliStatisticAdmin)

admin.site.register(MonthStatistic, MonthStatisticAdmin)
