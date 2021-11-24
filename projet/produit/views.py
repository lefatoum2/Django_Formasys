from django.shortcuts import render
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client

# Create your views here.
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {'commandes':commandes, 'clients': clients}
    return render(request, 'produit/acceuil.html', context)
