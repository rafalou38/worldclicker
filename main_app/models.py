from django.db import models
from django_countries.fields import CountryField
# Create your models here.

class custom_user(models.Model):

    nom = models.CharField(max_length=15)
    cliks = models.PositiveIntegerField(default=0)
    pays = CountryField()
    creation = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.nom
class world(models.Model):
	cliks = models.BigIntegerField(default=0)
	def __str__(self):
		return str(self.cliks)
    

    