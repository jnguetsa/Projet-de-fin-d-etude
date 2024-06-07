# filters.py
import django_filters
from .models import Sale

class SaleFilter(django_filters.FilterSet):
    Nom_malade = django_filters.CharFilter(lookup_expr='icontains')
    code_recu = django_filters.CharFilter(lookup_expr='icontains')
    date_rec = django_filters.DateFilter(lookup_expr='exact')

    class Meta:
        model = Sale
        fields = ['Nom_malade', 'code_recu', 'date_rec']
