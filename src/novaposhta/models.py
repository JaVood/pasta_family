from django.db import models
from django.utils.translation import ugettext_lazy as _


class Warehouse(models.Model):

    title = models.CharField(_('Title'), max_length=255, db_index=True)

    address = models.CharField(_('Address'), max_length=255, db_index=True)

    city = models.ForeignKey(
        to='City',
        related_name='warehouse',
        on_delete=models.SET_NULL,
        verbose_name=_('City'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Warehouse')
        verbose_name_plural = _('Warehouses')
        ordering = ['id']

class Area(models.Model):

    area = models.CharField(_('Area'), max_length=255, db_index=True, null=True)

    ref = models.CharField(_('Ref'), max_length=255, db_index=True, null=True)

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = _('Area')
        verbose_name_plural = _('Areas')
        ordering = ['id']


class City(models.Model):

    city = models.CharField(_('City'), max_length=255, db_index=True, null=True)

    area = models.CharField(_('Area'), max_length=255, db_index=True, null=True)

    area_id = models.ForeignKey(
        to='Area',
        related_name='city',
        on_delete=models.SET_NULL,
        verbose_name=_('Area'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ['id']
