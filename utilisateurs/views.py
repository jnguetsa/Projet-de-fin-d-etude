from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import redirect, render
from PRODUITS.models import RegistresDesEntrer
from  utilisateurs.forms import UserForm
from django.template.loader import render_to_string
from xhtml2pdf import pisa

# Create your views here.
def register(request):
    form= UserForm()
    if request.method == 'POST':
        form= UserForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'user/register.html', {'form':form})


