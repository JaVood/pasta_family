from django.contrib import admin
from pasta_family import models
from pasta_family import forms
from pasta_family.models import MainPhoto, AboutCompanyPhoto


@admin.register(models.User)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.UserForm


@admin.register(models.Product)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.ProductForm


@admin.register(models.ProductGroup)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.ProductGroupForm


@admin.register(models.Cooperation)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.CooperationForm


@admin.register(models.CooperationForm)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.CooperationFormForm


@admin.register(models.CooperationType)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.CooperationTypeForm


@admin.register(models.Review)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    form = forms.ReviewForm


@admin.register(models.ReviewNew)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.ReviewNewForm


@admin.register(models.ProductType)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.ProductTypeForm


@admin.register(models.ProductWeight)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.ProductWeightForm


@admin.register(models.Price)
class ProfileAdmin(admin.ModelAdmin):
    form = forms.PriceForm


class MainPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'ru_version']


admin.site.register(MainPhoto, MainPhotoAdmin)


class AboutCompanyPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']


admin.site.register(AboutCompanyPhoto, AboutCompanyPhotoAdmin)
