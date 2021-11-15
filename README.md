# Django 
## Installation
```
pip install django
```
Création d'un projet :
```
django-admin startproject projet
```
Création d'une application (produit, commande) :

```
django-admin startapp produit
```
```
django-admin startapp commande
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
]

```