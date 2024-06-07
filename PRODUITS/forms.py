from django import forms
from .models import Produit, ProduitVente, RegistresDesEntrer
from .constants import CONDITIONNEMENTS, FORMES_GALENIQUES

class ProduitForm(forms.ModelForm):
    num_lot = forms.IntegerField(label="",widget=forms.NumberInput(attrs={'class ': 'form-control ', 'placeholder': 'Num_lot'}))
    date_peremption = forms.DateField(label="", widget=forms.DateInput(attrs={'class ': 'form-control ', 'placeholder': "Date de peremption"}))

    nom = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': "Nom du medicament"}))
    code = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': "Code du produit"}))
    conditionnement = forms.ChoiceField(label="", choices=CONDITIONNEMENTS,widget=forms.Select(attrs={'class ': 'form-control ', 'placeholder': "Conditionnement"}))
    dosage = forms.CharField(label="", widget=forms.TextInput(attrs={'class ': 'form-control ', 'placeholder': "Dosage"}))
    forme_galenique = forms.ChoiceField(label="", choices=FORMES_GALENIQUES, widget=forms.Select(attrs={'class ': 'form-control ', 'placeholder': "Forme galenique"}))

    class Meta:
        model = Produit
        fields = ['num_lot', 'date_peremption', 'nom', 'code', 'conditionnement','dosage', 'forme_galenique']

        


        
class RDEForm(forms.ModelForm):
    date_entree = forms.DateField(label="", widget=forms.DateInput(attrs={'class': 'form-control  col-12', 'placeholder': "Date d'entrée"}))
    num_pvr = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class': 'form-control col-12 ', 'placeholder': 'Num PVR'}))
    num_bl = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class': 'form-control col-12', 'placeholder': 'Num BL'}))
    qte_recue = forms.IntegerField(label="",widget=forms.NumberInput(attrs={'class': 'form-control col-12', 'placeholder': 'Qte Recu'}))
    prix_unitaire = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class': 'form-control  col-12', 'placeholder': 'Prix Unitaire'}))
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label="", widget=forms.Select( attrs={'class': 'form-control col-12 ', 'placeholder': "Produit Pharmaceutique"}))

    class Meta:
        model = RegistresDesEntrer
        fields = ['date_entree', 'num_pvr', 'num_bl', 'qte_recue', 'produit', 'prix_unitaire' ]


class  ProduitVenteForm(forms.ModelForm):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label="Produits", widget=forms.Select( attrs={'class': 'form-control', 'placeholder': "Produit Pharmaceutique"}))
    qte= forms.IntegerField(label="",widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité commande'}))
    # annulees= forms.BooleanField(label="",widget=forms.BooleanField(attrs={'class': 'form-control'}))
    class Meta:
        model= ProduitVente
        fields = ['produit', 'qte']
        