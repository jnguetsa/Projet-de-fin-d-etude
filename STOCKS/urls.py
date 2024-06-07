
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from PRODUITS.views import addproduct, addproduct_vente, delete_rde, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('utilisateurs.urls')),
    path('', include('VENTES.urls')),
    path('', include('PRODUITS.urls')),
] 


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
