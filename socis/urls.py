# Django
from django.urls import path
from . views import SocisView, CrearSoci, BorrarSoci, EditarSoci, LListaImportar, CrearImportacio, ExempleImportacio
from socis import views as socis_views

urlpatterns = [
    path('', SocisView.as_view(), name="socis"),
    path('borrar/<int:pk>', BorrarSoci.as_view(), name="soci_borrar"),
    path('crear/', CrearSoci.as_view(), name="soci_crear"),
    path('editar/<int:pk>', EditarSoci.as_view(), name="soci_editar"),
    path('importar/', LListaImportar.as_view(), name="importacions"),
    path('importar-nova/', CrearImportacio.as_view(), name="importar_crear"),
    path('importar-exemple/<int:pk>', ExempleImportacio.as_view(), name="importar_exemple"),
]
