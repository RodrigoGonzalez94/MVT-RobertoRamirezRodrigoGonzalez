from django.urls import path
from .views import una_vista, un_template, listado_de_familiares

urlpatterns = [
    path('', una_vista),
    path('mi-template/', un_template),
    path('listado-de-familiares/', listado_de_familiares)
]