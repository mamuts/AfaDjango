from django.shortcuts import render
from django.views.generic.list import ListView
from .models import EstonesDia, EstonesUsuaris
from django.db.models import Count

# Create your views here.
class EstonesView(ListView):
    template_name = 'estones/estones_llista.html'
    login_url = "estones:login"
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context = super(EstonesView, self).get_context_data(**kwargs)
        num_usuaris = EstonesUsuaris.objects.count()
        context['socis'] = num_usuaris
        return context

    def get_queryset(self):
        value_list = EstonesDia.objects.values_list('usuari_id').distinct()
        group_by_value = {}
        for value in value_list:
            group_by_value[value] = EstonesUsuaris.objects.filter(usuari_id=value)

        #object_list = EstonesDia.objects.distinct()
        return group_by_value
