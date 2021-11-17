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