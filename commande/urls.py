
from django.urls import path
from . import views

urlpatterns = [

    path('',views.list_commande),
    path('ajout_commande/',views.ajouter_commande,name='ajout_commande')
]
