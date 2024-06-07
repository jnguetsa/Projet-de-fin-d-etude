import uuid
from django.db import models
from PRODUITS.models import ProduitVente
from django.contrib.auth import get_user_model

from STOCKS.settings import AUTH_USER_MODEL




class Sale(models.Model):
    pharmacien = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    date_rec= models.DateField()
    Nom_malade= models.CharField(max_length=100)
    code_recu= models.CharField(max_length=4, blank=True)
    produit = models.ManyToManyField(ProduitVente)
    
    prix_total= models.PositiveIntegerField(blank=True, null= True )
    

    def __str__(self):
            produits = ' ** '.join([str(item) for item in self.produit.all()])
            return f'Dare recette: {self.date_rec} - Nom: {self.Nom_malade} - Code: {self.code_recu} - {produits} - Prix total :{self.prix_total} '
    
    
    def save( self, *args, **kwargs):
        if self.code_recu=="":
            self.code_recu= str(uuid.uuid4()).replace('-','').upper()[:4]
            print("----------------------------------")
        return super().save(*args, **kwargs)