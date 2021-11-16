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
    'produit',
    'commande',
    'client',
]
```
## Les routes
projet/urls.py :

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produit.urls')),
    path('commande', include('commande.urls')),
    path('client', include('client.urls')),
]

```
Création de commande/urls.py :
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_commande),
]
```
commande/views.py :
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_commande(request):
    return HttpResponse('La liste des commandes:')

```
client/views.py : 
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_client),
]
```
Création de client/urls.py :
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_client(request):
    return HttpResponse('La liste des clients:')

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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
    return render(request,'produit/acceuil.html')

```


