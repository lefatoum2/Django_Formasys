
# Django 

## Sommaire 

* [1. Installation](#Section_1)
* [2. Les Routes](#Section_2)
* [3. Les Templates](#Section_3)
* [4. Création des modèles](#Section_4)
* [5. Afficher les données dans la partie frontend](#Section_5)
* [6. URLs dynamiques](#Section_6)
* [7. CRUD](#Section_7)
* [8. Implementation du filtre](#Section_8)
* [9. Inscription](#Section_9)
* [10. Login](#Section_10)
* [11. Logout](#Section_11)
* [12. Autorisation d'accès](#Section_12)

## 1. Installation<a class="anchor" id="section_1"></a>  

### Virtual Environmenent
```
virtualenv venv
```

Activate
```
venv/Scripts/activate
```

Save your configuration :
```
pip freeze > requirements.txt
```

### Django
```
pip install django
```
Création d'un projet :
```
django-admin startproject projet
```
Création d'une application (produit, commande, client) :

```
django-admin startapp produit
```
```
django-admin startapp commande
```
```
django-admin startapp client
```

projet/settings.py :

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produit', # ajout
    'commande', # ajout
    'client', # ajout
]
```
## 2. Les routes<a class="anchor" id="section_2"></a>
projet/urls.py :

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produit.urls')), # ajout
    path('commande', include('commande.urls')), # ajout
    path('client', include('client.urls')), # ajout
]

```
Création de commande/urls.py :
```python
from django.contrib import admin
from django.urls import path, include
from . import views # ajout

urlpatterns = [
    path('', views.list_commande), # ajout
]
```
commande/views.py :
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_commande(request):
    return HttpResponse('La liste des commandes:') # ajout

```
client/views.py : 
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_client), # ajout
]
```
Création de client/urls.py :
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_client(request):
    return HttpResponse('La liste des clients:') # ajout

```
produit/views.py :
```python
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Bienvenue')

```
Création de produit/urls.py :
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
]
```
## 3. Les templates<a class="anchor" id="section_3"></a>

Créez le dossier templates/produit et ensuite  templates/produit/acceuil.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Amazon</title>
</head>
<body>
    <h1> Accueil </h1>
</body>
</html>
```

Puis modifiez projet/settings.py :

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # ajout
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Et pour charger les fichiers css et les images, projet/settings.py:
```python
...
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/images/'
...
```
Charger css dans html : 
```html
{% load static %}
...
...
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
```


Puis modifiez produit/views.py : 

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'produit/acceuil.html') # ajout

```

Créez le fichier templates/base/navbar.html :
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">CRM</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Acceuil</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#">Produits</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Clients</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Commandes</a>
      </li>
    </ul>
  </div>
</nav>
```

puis templates/main.html :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Amazon</title>
    <!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

    <style>

		#logo{
		}

		body{
			background-color: #ebeff5;
		}


		#total-orders{
			background-color: #4cb4c7;
		}


		#orders-delivered{
			background-color: #7abecc;
		}

		#orders-pending{
			background-color: #7CD1C0;
		}




	</style>

</head>
<body>
{% include 'base/navbar.html' %}

{% block content %}
{% endblock content%}
<hr>
<h1>Footer</h1>
</body>
<!-- JS, Popper.js, and jQuery -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</html>
```

puis acceuil.html:

```html
{% extends 'main.html' %}


    {% block contenu%}

    <h1>Acceuil</h1>

    {% endblock %}
```

commande/list_commande.html
```html
{% extends 'main.html' %}


    {% block contenu%}

    <h1>La liste des commandes</h1>

    {% endblock %}
```

client/list_client.html
```html
{% extends 'main.html' %}


    {% block contenu%}

    <h1>La liste des clients</h1>

    {% endblock %}
```

produit/views.py :
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'produit/acceuil.html')

```

client/views.py :
```python
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def list_client(request):
    return render(request, 'client/list_client.html')

```

commande/views.py :
```python
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def list_commande(request):
    return render(request,'commande/list_commande.html')


```
produit/acceuil.html :

```html
{% extends 'main.html' %}

    {% block content%}
<br>
<div class="row">
    <div class="col-md-5">
        <h5>Clients:</h5>
        <hr>
        <div class="card card-body">
            <a class="btn btn-primary btn-sm btn-block" href="">Créer Un Client</a>
            <table class="table table-sm">
                <tr>
                    <th></th>
                    <th>Clients</th>
                    <th>Commandes</th>
                </tr>

            </table>
        </div>
    </div>

    <div class="col-md-7">
        <h5>Les 5 Dernières Commandes</h5>
        <hr>
        <div class="card card-body">
            <a class="btn btn-primary btn-sm btn-block" href="">Ajouter une Commande</a>
            <table class="table table-sm">
                <tr>
                    <th>Produit</th>
                    <th>Date de la commande</th>
                    <th>Status</th>
                    <th>Mise à jour</th>
                    <th>Supprimer</th>
                </tr>
            </table>
        </div>

    </div>


</div>
    {% endblock content%}
```

## 4. Création des modèles<a class="anchor" id="section_4"></a>

commande/models.py
```python
import sys
from django.db import models
from produit.models import Produit
from client.models import Client


# Create your models here.
class Commande(models.Model):
    STATUS = (('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré"'))
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True,choices=STATUS)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.produit.name

```
client/models.py
```python
from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.nom
```
produit/models.py
```python
from django.db import models


# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(null=True)

    def __str__(self):
        return self.nom
```

```python 
python manage.py makemigrations
```

```python 
python manage.py migrate
```
### Création du superadministrateur

```python
python manage.py createsuperuser
```

#### Ajouter une table dans admin (partie administrateur)

client/admin.py
```python
from django.contrib import admin
from .models import Client

# Register your models here.
admin.site.register(Client)
```

commande/admin.py
```python
from django.contrib import admin
from .models import Commande
# Register your models here.

admin.site.register(Commande)

```
produit/admin.py
```python
from django.contrib import admin
from .models import Produit
# Register your models here.

admin.site.register(Produit)
```
##  5. Afficher les données dans la partie frontend<a class="anchor" id="section_5"></a>

produit/views.py :
```python
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

```

templates/produit/acceuil.html :

```html
{% extends 'main.html' %}

    {% block content%}
<br>
<div class="row">
    <div class="col-md-5">
        <h5>Clients:</h5>
        <hr>
        <div class="card card-body">
            <a class="btn btn-primary btn-sm btn-block" href="">Créer Un Client</a>
            <table class="table table-sm">
                <tr>
                    <th>ID</th>
                    <th>Clients</th>
                    <!--<th>Commandes</th>-->
                    <th>Telephone</th>

            {% for client in clients %}  <!--Ajout-->
                </tr>
                <th>{{client.id}}</th> <!--Ajout-->
                <th>{{client.nom}}</th> <!--Ajout-->
                <th>{{client.telephone}}</th> <!--Ajout-->
                {% endfor %} # <!--Ajout-->
            </table>
        </div>
    </div>

    <div class="col-md-7">
        <h5>Toutes les  Commandes</h5>
        <hr>
        <div class="card card-body">
            <a class="btn btn-primary btn-sm btn-block" href="">Ajouter une Commande</a>
            <table class="table table-sm">
                <tr>
                    <th>Produit</th>
                    <th>Date de la commande</th>
                    <th>Status</th>
                    <th>Mise à jour</th>
                    <th>Supprimer</th>
                </tr>
                {% for commande in commandes %} <!--Ajout-->
                <tr>
                    <th>{{commande.produit}}</th> <!--Ajout-->
                    <th>{{commande.client}}</th> <!--Ajout-->
                    <th>{{commande.date_creation}}</th> <!--Ajout-->
                    <th>{{commande.status}}</th> <!--Ajout-->
                    <th><a href = ''> Mettre à jour</a></th> <!--Ajout-->
                    <th><a href = ''>Supprimer</a></th> <!--Ajout-->

                </tr>
                {% endfor %} <!--Ajout-->
            </table>
        </div>

    </div>


</div>
    {% endblock content%}
```

## 6. URLs dynamiques<a class="anchor" id="section_6"></a>

client/views.py :
```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client


# Create your views here.
def list_client(request, pk):
    client = Client.objects.get(id=pk) #  Ajout
    commande = client.commande_set.all() #  Ajout
    commande_total = commande.count() #  Ajout
    context = {'client': client, 'commande': commande, 'commande_total': commande_total} #  Ajout
    return render(request, 'client/list_client.html', context) #  Ajout
```
client/urls.py :
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/<str:pk>', views.list_client, name='client'), # Ajout
]
````

client/list_client.html :

```html
{% extends 'main.html' %}

    {% block content %}

    <h1>La liste des clients</h1>
    <div class="col-md">
        <div class="row">
            <div class="card card-body">

                <form method="get">
                    <button class="btn btn-primary" type="submit">Modifier le client</button>
                    <button class="btn btn-primary" type="submit">Supprimer le client</button>
                </form>
            </div>
        </div>


        </div>
        <div class="card card-body">
            <h5>Informations</h5>
            <hr>
            <p>Nom : {{client.nom}}</p>
            <p>Telephone: {{client.telephone}}</p>
        </div>

        <div>
            <table class="table table-sm">
            <tr>
                <th>Produit</th>
                <th>Categorie</th>
                <th>Date de commande</th>
                <th>Status</th>
                <th>Mise à jour</th>
                <th>Supprimer</th>

            </tr>
            {% for commande in commande %}
            <tr>
                <th>{{ commande.produit}}</th>
                <th>{{ commande.produit}}</th>
                <th>{{ commande.date_creation}}</th>
                <th>{{ commande.status}}</th>
                <th><a href=" ">Mise à jour</a></th>
                <th><a href=" ">Supprimer</a></th>

            </tr>
            {% endfor %}
            </table>
        </div>

        <div class="col-md">
            <div class="card card-body">
                <h5>Total des commandes</h5>
                    <hr>
                    <h1 style="text-align:center; padding: 10px">{{commande_total}}</h1>

        </div>

    </div>

    {% endblock content %}
```
## 7. CRUD<a class="anchor" id="section_7"></a>

Créer le formulaire pour ajouter une commande (commande/forms.py):
```python
from django.forms import ModelForm
from .models import Commande


class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
```

Puis commande/views.py :

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommandeForm
from .models import Commande


# Create your views here.
def list_commande(request):
    return render(request, 'commande/list_commande.html')


def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


def modifier_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


def supprimer_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context = {'item': commande}
    return render(request, 'commande/supprimer_commande.html', context)

```

commande/ajouter_commande.html :

```html
{% extends 'main.html' %}


    {% block content %}

    <h1>Ajouter une commande</h1>
<div class="row">
<div class="col-md-6">
    <div class="card card-body">
    <form action="" method="POST">
        {% csrf_token %}
        {{form}}
        <input type="submit" name="Envoyer">
    </form>
    </div>
    </div>
</div>
    {% endblock content %}
```

commande/supprimer_commande.html :

```html
{% extends 'main.html' %}


    {% block content %}

    <h1>Supprimer commande</h1>
    <p>Voules-vous supprimer cette commande</p>
<form action="{% url 'supprimer_commande' item.id%}" method="POST"></form>
            {% csrf_token %}
            <a class="btn btn-warning" href="{% url 'acceuil' %}">Annuler</a>
            <input class="btn btn-danger" type="submit" name="Confirmer">
    {% endblock content %}
```
produit/acceuil.html:

```html
{% extends 'main.html' %}

    {% block content%}
<br>
<div class="row">
    <div class="col-md-5">
        <h5>Clients:</h5>
        <hr>
        <div class="card card-body">
            <a class="btn btn-primary btn-sm btn-block" href="">Créer Un Client</a>
            <table class="table table-sm">
                <tr>
                    <th>ID</th>
                    <th>Clients</th>
                    <!--<th>Commandes</th>-->
                    <th>Telephone</th>
                    <th>Details</th>

            {% for client in clients %}
                </tr>
                <th><a href="{% url 'client' client.id %}">{{client.id}}</a></th>
                <th>{{client.nom}}</th>
                <th>{{client.telephone}}</th>
                <th><a class="btn btn-sm btn-info" href="{% url 'client' client.id %}">Details</a></th>
                {% endfor %}
            </table>
        </div>
    </div>

    <div class="col-md-7">
        <h5>Toutes les  Commandes</h5>
        <hr>
        <div class="card card-body">
            <a class="btn btn-primary btn-sm btn-block" href="{% url 'ajout_commande' %}">Ajouter une Commande</a>
            <table class="table table-sm">
                <tr>
                    <th>Produit</th>
                    <th>Date de la commande</th>
                    <th>Status</th>
                    <th>Mise à jour</th>
                    <th>Supprimer</th>
                </tr>
                {% for commande in commandes %}
                <tr>
                    <th>{{commande.produit}}</th>
                    <th>{{commande.client}}</th>
                    <th>{{commande.date_creation}}</th>
                    <th>{{commande.status}}</th>
                    <th><a class="btn btn-sm btn-info" href="{% url 'modifier_commande' commande.id %}">Modifier</a></th>
                    <th><a class="btn btn-sm btn-danger" href="{% url 'supprimer_commande' commande.id %}">Supprimer</a></th>


                </tr>
                {% endfor %}
            </table>
        </div>

    </div>


</div>
    {% endblock content%}
```
produit/urls.py:

```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'acceuil'),
]

```

## 8. Implementation du filtre<a class="anchor" id="section_8"></a>

```python
pip install django_filters
```

settings.py :

```python
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produit',
    'commande',
    'client',
    'django_filters',
]
...
```
client/views.py :

```python
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


```

client/list_client.html:

```html
...
<div class="row">
            <div class="col">
                <div class="card card-body">
                    <form method="get">
                        <button class="btn btn-primary" type="submit">Search</button>
                        {{myFilter.form}}
                    </form>
                </div>
            </div>
        </div>

...
```
## 9. Inscription<a class="anchor" id="section_9"></a>

```python
py manage.py startapp compte
```

settings.py:
```python
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produit',
    'commande',
    'client',
    'django_filters',
    'compte', # ajout
]
```
projets/urls.py  :

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produit.urls')),
    path('commande', include('commande.urls')),
    path('client', include('client.urls')),
    path('compte', include('compte.urls')),
]
```

compte/urls.py : 
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('inscription', views.inscriptionPage, name='inscription'),
    path('acces', views.accesPage, name='acces'),
]

```

compte/views.py :
```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib import messages

# Create your views here.

def inscriptionPage(request):
    form = CreerUtilisateur
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte crée  avec succès pour ' + user)
            return redirect('acces')
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def accesPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.info(request, 'Erreur dans le mot de passe ou le nom d\'utilisateur')
    return render(request, 'compte/access.html')

```

Création de compte/forms.py :
```python
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

```

templates/compte/inscription.html :
```html
<!DOCTYPE html>
<html>

<head>
	<title>Login</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">

	<style>
		body,
		html {
			margin: 0;
			padding: 0;
			height: 100%;
			background: #7abecc !important;
		}
		.user_card {
			width: 350px;
			margin-top: auto;
			margin-bottom: auto;
			background: #74cfbf;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;

		}

		.form_container {
			margin-top: 20px;
		}

		#form-title{
			color: #fff;
		}
		.login_btn {
			width: 100%;
			background: #33ccff !important;
			color: white !important;
		}
		.login_btn:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}
		.login_container {
			padding: 0 2rem;
		}
		.input-group-text {
			background: #f7ba5b !important;
			color: white !important;
			border: 0 !important;
			border-radius: 0.25rem 0 0 0.25rem !important;
		}
		.input_user,
		.input_pass:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}

	</style>

</head>
<body>
	<div class="container h-100">
		<div class="d-flex justify-content-center h-100">
			<div class="user_card">
				<div class="d-flex justify-content-center">
					<h3 id="form-title">INSCRIPTION</h3>
				</div>
				<div class="d-flex justify-content-center form_container">

					<form method="POST" action="">
                        {%csrf_token%}
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-user"></i></span>
							</div>
							{{form.username}}
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-envelope-square"></i></span>
							</div>
							{{form.email}}
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
							{{form.password1}}
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
							{{form.password2}}
						</div>
                        {{form.errors}}
				   		<div class="d-flex justify-content-center mt-3 login_container">
				 			<input class="btn login_btn" type="submit" value="S'inscrire">
				   		</div>
					</form>
				</div>

				<div class="mt-4">
					<div class="d-flex justify-content-center links">
						Avez-vous un compte? <a href="{% url 'acces' %}" class="ml-2">Se connecter</a>
					</div>
				</div>
			</div>
		</div>
	</div>
	<script>
						/* Because i didnt set placeholder values in forms.py they will be set here using vanilla Javascript
		//We start indexing at one because CSRF_token is considered and input field
		 */

		//Query All input fields
		var form_fields = document.getElementsByTagName('input')
		form_fields[1].placeholder='Nom d'utilisateur..';
		form_fields[2].placeholder='Email..';
		form_fields[3].placeholder='Mot de passe...';
		form_fields[4].placeholder='Confirmer...';


		for (var field in form_fields){
			form_fields[field].className += ' form-control'
		}
	</script>
</body>
</html>
```

## 10. Login<a class="anchor" id="#Section_10"></a>


templates/compte/access.html :
```html
<!DOCTYPE html>
<html>

<head>
	<title>Accès</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">


	<style>
		body,
		html {
			margin: 0;
			padding: 0;
			height: 100%;
			background: #7abecc !important;
		}
		.user_card {
			width: 350px;
			margin-top: auto;
			margin-bottom: auto;
			background: #74cfbf;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;

		}

		.form_container {
			margin-top: 20px;
		}

		#form-title{
			color: #fff;

		}

		.login_btn {
			width: 100%;
			background: #33ccff !important;
			color: white !important;
		}
		.login_btn:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}
		.login_container {
			padding: 0 2rem;
		}
		.input-group-text {
			background: #f7ba5b !important;
			color: white !important;
			border: 0 !important;
			border-radius: 0.25rem 0 0 0.25rem !important;
		}
		.input_user,
		.input_pass:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}

		#messages{
			background-color: grey;
			color: #fff;
			padding: 10px;
			margin-top: 10px;
		}
	</style>

</head>
<body>
	<div class="container h-100">
		<div class="d-flex justify-content-center h-100">
			<div class="user_card">
				<div class="d-flex justify-content-center">


					<h3 id="form-title">LOGIN</h3>
				</div>
				<div class="d-flex justify-content-center form_container">
					<form method="POST" action="">
						{%csrf_token%}
						<div class="input-group mb-3">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-user"></i></span>
							</div>
							<input type="text" name="username" placeholder="Nom d'utilisateur..." class="form-control">
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
								<input type="password" name="password" placeholder="Mot de passe..." class="form-control" >
						</div>

							<div class="d-flex justify-content-center mt-3 login_container">
				 				<input class="btn login_btn" type="submit" value="Se connecter">
				   			</div>
					</form>

				</div>
				{% for message in messages %}
				<p id="messages">{{message}}</p>
				{% endfor%}
				<div class="mt-4">
					<div class="d-flex justify-content-center links">
						Avez-vous un compte? <a href="{% url 'inscription' %}" class="ml-2">Inscrivez-vous</a>
					</div>

				</div>
			</div>
		</div>
	</div>
</body>

</html>
```

## 11. Logout<a class="anchor" id="section_11"></a> 

compte/views.py :

```python
...
def logoutUser(request):
    logout(request)
    return redirect('acces')
```

compte/urls.py:
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('inscription', views.inscriptionPage, name='inscription'),
    path('acces', views.accesPage, name='acces'),
    path('quitter', views.logoutUser, name='quitter')
]

```

Bouton quitter dans templates/base/navbar.html :
```html
{% load static %}
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <img src="{% static 'images/logo.png' %}">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Acceuil</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#">Produits</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Clients</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Commandes</a>
      </li>
    </ul>
  </div>
  <span>Salut, {{request.user}} </span>
  <span><a href="{% url 'quitter' %}"> Quitter</a></span>
</nav>
```

### 12. Autorisation d'accès<a class="anchor" id="section_12"></a>

produit/views.py:
```python
from django.shortcuts import render
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='acces')
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {'commandes':commandes, 'clients': clients}
    return render(request, 'produit/acceuil.html', context)

```

commande/views.py:
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommandeForm
from .models import Commande
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='acces')
def list_commande(request):
    return render(request, 'commande/list_commande.html')

@login_required(login_url='acces')
def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)

@login_required(login_url='acces')
def modifier_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)

@login_required(login_url='acces')
def supprimer_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context = {'item': commande}
    return render(request, 'commande/supprimer_commande.html', context)

```
Source: https://www.youtube.com/watch?v=h7cOL9JK-Gs&list=PL5waSwMME4E7_lbB6BcluIiqCsU0uW2Zm
