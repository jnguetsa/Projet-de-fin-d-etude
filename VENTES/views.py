from django.shortcuts import redirect, render
from VENTES.filters import SaleFilter
from VENTES.forms import SaleForm
from VENTES.models import Sale
from django.shortcuts import render, get_object_or_404
from xhtml2pdf import pisa
from django.http import HttpResponse
from .models import Sale
from io import BytesIO
# Create your views here.
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

# @login_required

def sale(request):
    sales = Sale.objects.all()
    
    if request.method == 'POST':
        form1 = SaleForm(request.POST)
        if form1.is_valid():
            sale_instance = form1.save(commit=False)
            sale_instance.pharmacien = request.user
            
            sale_instance.save()
            form1.save_m2m()  # Save Many-to-Many relationships
            
            return redirect('sale')  # Redirect to the 'sale' view after saving
    else:
      form1 = SaleForm()
    context = {
        'form1': form1,
        'sales': sales,
        
    }

    return render(request, 'pharmaciens.html', context)



def search_sales(request):
    sales_list = Sale.objects.all()
    sale_filter = SaleFilter(request.GET, queryset=sales_list)

    if request.htmx:
        html_content = render_to_string('sales_list.html', {'sales': sale_filter.qs, 'filter': sale_filter})
        return HttpResponse(html_content)

    return render(request, 'search_sales.html', {'filter': sale_filter})



def generate_sale_pdf(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    html = render_to_string('sale_pdf.html', {'sale': sale})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="sale_{sale_id}.pdf"'
    result = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=response)
    if result.err:
        return HttpResponse('Error generating PDF: %s' % result.err, status=400)
    return response




@csrf_exempt
def delete_sale(request, id):
    if request.method == 'DELETE':
        delete_id = int(id)
        instance = get_object_or_404(Sale, pk=delete_id)
        instance.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

