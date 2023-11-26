from django.contrib import admin
from .models import Socis, Importar

# Register your models here.
class SocisAdmin(admin.ModelAdmin):
    list_display = ["soci_nom", "soci_curs", "soci_email"]
    fields = [("soci_nom", "soci_curs"), "soci_email"]


admin.site.register(Socis, SocisAdmin)

admin.site.register(Importar)
