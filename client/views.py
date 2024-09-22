from django.shortcuts import render
from .models import Client

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_client(request, pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total = commande.count()
    context={'client':client,'commande' :commande,'commande_total' :commande_total}
    return render(request, 'client/list_client.html', context)
