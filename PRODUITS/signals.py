
from datetime import date
from django.db.models.signals import post_save

from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db import transaction
from VENTES.models import Sale
from .models import RegistresDesEntrer, ProduitVente, Stock_en_peremption





@receiver(post_save, sender=ProduitVente)
def migrer_donnees_vers_recette(sender, instance, created, **kwargs):
    if created:
        try:
            RDE = RegistresDesEntrer.objects.get(produit=instance.produit)

            instance.prix_unitaire = RDE.prix_unitaire
            instance.prix_total = instance.prix_unitaire * instance.qte

            # Mise à jour de qte_recu dans RegistreDesEntrer
            RDE.qte_recue = RDE.qte_recue - instance.qte
            RDE.save()
            instance.save()

        except ObjectDoesNotExist:
            print("Aucune instance de RegistreDesEntrer trouvée pour les valeurs spécifiées.")

    # Vérifier si la vente est annulée
    if instance.annulees:
        # Si la vente est annulée, ajuster la quantité reçue
        try:
            RDE = RegistresDesEntrer.objects.get(produit=instance.produit)
            RDE.qte_recue = RDE.qte_recue + instance.qte
            RDE.save()
        except ObjectDoesNotExist:
            return HttpResponse('')
        







