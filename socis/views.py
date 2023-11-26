import csv
import os

from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Socis, Importar
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SocisView(LoginRequiredMixin, ListView):
    template_name = 'socis/socis_llista.html'
    # login_url = "socis:login"
    context_object_name = "obj"
    model = Socis

    def get_context_data(self, **kwargs):
        context = super(SocisView, self).get_context_data(**kwargs)
        num_usuaris = Socis.objects.count()
        context['socis'] = num_usuaris
        return context

class CrearSoci(CreateView):
    model = Socis
    template_name = "socis/socis_crear.html"
    context_object_name = "obj"
    fields = '__all__'
    success_url = reverse_lazy("socis:socis")

class BorrarSoci(DeleteView):
    model = Socis
    template_name = "socis/socis_borrar.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socis:socis")

class EditarSoci(UpdateView):
    model = Socis
    fields = '__all__'
    template_name = "socis/socis_editar.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socis:socis")

class LListaImportar(ListView):
    """docstring for LListaImportar"""
    model = Importar
    template_name = "socis/importar_llista.html"
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context = super(LListaImportar, self).get_context_data(**kwargs)
        context['socis'] = 200
        return context

class CrearImportacio(CreateView):
    """docstring for CrearImportacio"""
    model = Importar
    context_object_name = "obj"
    fields = '__all__'
    template_name = "socis/importar_crear.html"
    success_url = reverse_lazy("socis:importacions")

class ExempleImportacio(View):
    """ Classe per mostrar la primera línia de dades a importar i permetre a l'usuari contralar aquesta importació """
    def get(self, request, *args, **kwargs):
        socis = []
        id = self.kwargs['pk']
        importacio = Importar.objects.filter(importar_id=id).first()
        path = str(importacio.importar_ruta)
        #Eliminem els 10 primers caracters perque indiquen el directori afadjango
        ruta = os.path.join(settings.BASE_DIR, path[10:])
        with open(ruta, "r") as csv_file:
            data = list(csv.reader(csv_file, delimiter=","))
            for row in data[1:]:
                socis.append(
                    Socis(
                        soci_nom=row[0],
                        soci_curs =row[1],
                        soci_direccio =row[2],
                        soci_codi_postal = row[3],
                        soci_ciutat  = row[4],
                        soci_telefon = row[5],
                        soci_email = row[6],
                        soci_drets_imatge = row[7],
                        soci_drets_whatzap = row[8],
                        soci_cc = row[9],
                        soci_nom_pares = row[10],
                    )
                )
        if len(socis) > 0:
            Socis.objects.bulk_create(socis)
        return HttpResponseRedirect(reverse_lazy("socis:socis"))
