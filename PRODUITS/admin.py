from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Produit,  RegistresDesEntrer, ProduitVente, Rupture_de_stock, Stock_en_peremption

admin.site.register(Produit)
#admin.site.register(BaseProduit)

admin.site.register(ProduitVente)


admin.site.register(RegistresDesEntrer)
admin.site.register(Rupture_de_stock)
admin.site.register(Stock_en_peremption)
