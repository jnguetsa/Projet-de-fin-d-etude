from django import forms
from VENTES.models import Sale

from PRODUITS.models import ProduitVente


class SaleForm(forms.ModelForm):
    date_rec = forms.DateField(label="", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': "Date d'entrée"}))
    Nom_malade = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom du malade"}))
    produit = forms.ModelMultipleChoiceField(queryset=ProduitVente.objects.all(), label="", widget=forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': "Produits"}))

    class Meta:
        model = Sale
        fields = ["date_rec", "Nom_malade", "produit"]


