from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_save

from django.dispatch import receiver

from PRODUITS.models import RegistresDesEntrer
from .models import Sale


# Le signal `m2m_changed` est déclenché lorsque la relation ManyToMany `produit` est modifiée.
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=Sale.produit.through)
def update_prix_total(sender, instance, action, **kwargs):

    total = 0

    # Parcourir tous les produits associés à cette vente
    for produit_vente in instance.produit.all():
        
        # Ajouter au total le prix unitaire multiplié par la quantité
        total += produit_vente.qte * produit_vente.prix_unitaire

    # Mettre à jour le champ prix_total de l'instance Sale après avoir calculé le total de tous les produits
    instance.prix_total = total
    
    # Sauvegarder l'instance pour enregistrer le nouveau prix total
    instance.save()
    
