
from django.urls import path

from VENTES.views import delete_sale, generate_sale_pdf, sale, search_sales


urlpatterns=[
    path('sale',sale,name='sale'),
    path('delete_sale/<int:id>/', delete_sale, name='delete_sale'),
    path('search/', search_sales, name='search_sales'),
    path('generate-sale-pdf/<int:sale_id>/', generate_sale_pdf, name='generate_sale_pdf'),
 

    
    
]