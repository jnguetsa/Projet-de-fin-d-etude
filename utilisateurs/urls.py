
from django.urls import path
from PRODUITS.views import gestionnaire, home, personne, pharmacien
from utilisateurs.views import  register


urlpatterns=[ 
    path('', home, name='home'),
    path('pharmaciens', pharmacien, name='pharmacien'),
    path('gestionnaire', gestionnaire, name='gestionnaire'),
    path('personne', personne, name='personne'),
    path('register', register, name='register'),
    
    ] 