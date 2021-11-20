from django.db import models


# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(null=True)

    def __str__(self):
        return self.nom
