# models.py in PRODUITS
from django.db import models
from .constants import CONDITIONNEMENTS, FORMES_GALENIQUES
from django.contrib.auth import get_user_model


class BaseProduit(models.Model):
    User = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    num_lot = models.IntegerField( verbose_name="Numéro de lot")
    date_peremption = models.DateField(verbose_name="Date de péremption")
    nom = models.CharField(max_length=255, verbose_name="Nom")
    code = models.CharField(max_length=255, null=True, blank=True, verbose_name="Code")
    conditionnement = models.CharField(max_length=255, choices=CONDITIONNEMENTS, verbose_name="Conditionnement")
    dosage = models.CharField(max_length=255, verbose_name="Dosage")
    forme_galenique = models.CharField(max_length=255, choices=FORMES_GALENIQUES, verbose_name="Forme galénique")
    

    class Meta:
        abstract = True

    def __str__(self):
        return f" {self.nom} -  {self.conditionnement} -  {self.dosage} -  {self.forme_galenique} -  {self.date_peremption}"

class Produit(BaseProduit):
    pass

class ProduitVente(models.Model):
    User = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="Produit")
    qte = models.PositiveIntegerField(verbose_name="Quantité")
    prix_unitaire = models.PositiveBigIntegerField(blank=True, verbose_name="Prix unitaire", null=True)
    annulees = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.produit} - Prix unitaire :{self.prix_unitaire} - Quantites: {self.qte} - statut: {self.annulees} "
    
    
class RegistresDesEntrer(models.Model):
    User = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    date_entree = models.DateField(verbose_name="Date d'entrée")
    num_pvr = models.IntegerField(verbose_name="Numéro PVR")
    num_bl = models.IntegerField(verbose_name="Numéro BL")
    qte_recue = models.PositiveIntegerField(default=0, verbose_name="Quantité reçue")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="Produit")
    prix_unitaire = models.PositiveBigIntegerField(verbose_name="Prix unitaire")

    def __str__(self):
        return f"Date: {self.date_entree} - PVR: {self.num_pvr} - BL: {self.num_bl} - Quantité: {self.qte_recue} - {self.produit} - prix unitaire :{self.prix_unitaire}"


class Rupture_de_stock(models.Model):
    date_rup= models.DateField(null=True)
    nom = models.CharField(max_length=255, verbose_name="Nom")
    code = models.CharField(max_length=255, null=True, blank=True, verbose_name="Code")
    conditionnement = models.CharField(max_length=255, choices=CONDITIONNEMENTS, verbose_name="Conditionnement")
    dosage = models.CharField(max_length=255, verbose_name="Dosage")
    forme_galenique = models.CharField(max_length=255, choices=FORMES_GALENIQUES, verbose_name="Forme galénique")
    
    def __str__(self) -> str:
        return f'{self.nom}'
    
class Stock_en_peremption(models.Model):
    date_peremp= models.DateField( null=True , blank=True)
    nom = models.CharField(max_length=255, verbose_name="Nom",  null=True , blank=True)
    conditionnement = models.CharField(max_length=255, choices=CONDITIONNEMENTS, verbose_name="Conditionnement", null=True , blank=True)
    forme_galenique = models.CharField(max_length=255, choices=FORMES_GALENIQUES, verbose_name="Forme galénique" , null=True , blank=True)
    num_lot= models.IntegerField(null=True, blank=True)
    qte = models.PositiveIntegerField(verbose_name="Quantité", null=True)
    
    prix_unitaire = models.PositiveBigIntegerField(verbose_name="Prix unitaire", null=True, blank=True)
    prix_perte = models.PositiveBigIntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.nom}'
    
    
