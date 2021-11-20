from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def list_commande(request):
    return render(request,'commande/list_commande.html')
