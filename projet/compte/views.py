from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur

# Create your views here.

def inscriptionPage(request):
    form = CreerUtilisateur(request.POST)
    context = {'form':form}
    return render(request, 'compte/inscription.html', context)


def accesPage(request):
    context = {}
    return render(request, 'compte/access.html')
