from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string


from .constants import CONDITIONNEMENTS, FORMES_GALENIQUES
from PRODUITS.forms import ProduitForm, ProduitVenteForm, RDEForm
from PRODUITS.models import Produit, ProduitVente, RegistresDesEntrer, Stock_en_peremption
from django.db import transaction


# Create your views here.



def home(request):
    error=''
    if request.method== 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            if user.pharmaciens:
               return redirect('sale')
                
            elif user.gestionnaires:
              return  redirect('gestionnaire')
            else:
               return redirect('personne')

        else:
            error= 'mot de passe ou username incorrect'
    return render(request, 'user/login.html', {'error':error})


def logout_user(request):
    logout(request)
    return redirect('home')

def pharmacien(request):
    return render(request, 'pharmaciens.html')

def gestionnaire(request):
    return render(request, 'gestionnaire.html')

def personne(request):
    return render(request, 'user/invite.html')            

def gestionnaire(request):
    entre = RegistresDesEntrer.objects.all().filter(qte_recue__gt= 1)[:5]

    if request.method == 'POST':
        form1 = RDEForm(request.POST)
        if form1.is_valid():
            rde_instance = form1.save(commit=False)
            rde_instance.User = request.user
            rde_instance.save()
            # Rediriger vers la page d'accueil après avoir enregistré les données
            form1.save()
            return redirect('gestionnaire')
        else:
            # Le formulaire n'est pas valide, donc rendre à nouveau la page avec les erreurs
            context = {'entre': entre, 'form1': form1}
            return render(request, 'gestionnaire.html', context)
    else:
        form1 = RDEForm()

    # Récupérer les données existantes pour affichage
    context = {'entre': entre, 'form1': form1}

    return render(request, 'gestionnaire.html', context)




def edit_rde(request, pk):
    rde = RegistresDesEntrer.objects.get(id=pk)
    if request.method == 'POST':
        form1 = RDEForm(request.POST, instance=rde)
        if form1.is_valid():
            edit_rde_instance= form1.save(commit=False)
            edit_rde_instance.User= request.user
            edit_rde_instance.save()
            form1.save()
            return redirect("gestionnaire")
            # Rediriger l'utilisateur vers une autre vue ou faire autre chose après la modification réussie

    else:
        form1= RDEForm(instance=rde)

    return render(request, 'edit_rde.html', {'form1': form1})



@csrf_exempt
def delete_rde(request, id):
    if request.method == 'DELETE':
        delete_id = int(id)
        instance = get_object_or_404(RegistresDesEntrer, pk=delete_id)
        instance.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
 
    
def addproduct(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            add_instace= form.save(commit= False)
            add_instace.User= request.user
            add_instace.save()
            form.save()
            return redirect('addproduct')
    else:
        product = Produit.objects.all()
        form = ProduitForm()

    context = {'form': form, 'product': product}
    return render(request, 'addproduct.html', context)

@login_required
def addproduct_vente(request):
    if request.method == 'POST':
        form = ProduitVenteForm(request.POST)
        if form.is_valid():
            add_sale_instace= form.save(commit= False)
            add_sale_instace.User= request.user
            add_sale_instace.save()
            form.save()
            return redirect('addproduct_sale')
    else:
        product = ProduitVente.objects.all()
        form = ProduitVenteForm()

    context = {'form': form, 'product': product}
    return render(request, 'addproduct_sale.html', context)

def rde_pdf(request):
    rde = RegistresDesEntrer.objects.all()
    html = render_to_string('rde_pdf.html', {'produit': rde})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rde.pdf"'
    result = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=response)
    if result.err:
        return HttpResponse('Error generating PDF: %s' % result.err, status=400)
    return response


