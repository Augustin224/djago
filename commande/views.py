from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_commande(request):
    return render(request, 'commande/list_commande.html')

def ajouter_commande(request):
    return render(request, 'commande/ajouter_commande.html')