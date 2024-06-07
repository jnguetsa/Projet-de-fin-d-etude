import django_filters

from .models import RegistresDesEntrer


class RDE(django_filters.filterset):
      date_entree = django_filters.DateFilter(lookup_expr='exact')
      num_pvr= django_filters.I
      
      Nom_malade = django_filters.CharFilter(lookup_expr='icontains')
      




