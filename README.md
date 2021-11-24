# Django 
## Installation
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
## Les routes
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
## Les templates

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

## Création des modèles

commande/models.py
```python
from django.db import models

# Create your models here.
class Commande(models.Model):
    STATUS = (('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré"'))
    # client =
    # produit =
    status = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

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
##  Afficher les données dans la partie frontend

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

## URLs dynamiques

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
