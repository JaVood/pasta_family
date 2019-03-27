from modeltranslation.translator import translator

from novaposhta.models import Warehouse, Area, City


translator.register(Warehouse, fields=['title', 'address'])

translator.register(Area, fields=['area', 'ref'])

translator.register(City, fields=['area', 'city'])
