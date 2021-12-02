from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from commande.filters import CommandeFiltre

# Create your views here.
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    myFilter = CommandeFiltre(request.GET,queryset=commande)
    commande=myFilter.qs
    context = {'client': client, 'commande': commande, 'commande_total': commande_total, 'myFilter':myFilter}
    return render(request, 'client/list_client.html', context)

