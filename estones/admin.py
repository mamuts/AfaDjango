from django.contrib import admin
from .models import EstonesUsuaris, EstonesQuotes, EstonesDia

# Register your models here.
admin.site.register(EstonesUsuaris)
admin.site.register(EstonesQuotes)
admin.site.register(EstonesDia)
