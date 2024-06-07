


from django.urls import path

from PRODUITS.views import addproduct, addproduct_vente, delete_rde, edit_rde, logout_user, rde_pdf


urlpatterns=[

    path('edit/<int:pk>/', edit_rde, name='edit_rde'),
    path('delete_rde/<int:id>/', delete_rde, name='delete_rde'),
    path('produits', addproduct, name='addproduct'),
    path('addproduct_vente', addproduct_vente, name='addproduct_sale'),
    path('logout_user', logout_user, name='logout_user'),
    path('rde_pdf', rde_pdf, name='rde_pdf'),
    
    
     ]