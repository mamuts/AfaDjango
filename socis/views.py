import csv

from django.conf import settings
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Socis, Importar
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
class SocisView(ListView):
    template_name = 'socis/socis_llista.html'
    login_url = "socis:login"
    context_object_name = "obj"
    model = Socis

    def get_context_data(self, **kwargs):
        context = super(SocisView, self).get_context_data(**kwargs)
        context['socis'] = 200
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
