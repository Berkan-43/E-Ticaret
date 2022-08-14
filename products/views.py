from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    urunler = UrunForm.objects.all()
    # Search
    search_product = ''
    if request.GET.get('search_product'):
        search_product = request.GET.get('search_product')
        urunler = urunler.filter(aciklama__icontains = search_product)
    context = {
        'urunler':urunler,
        'search_product':search_product
    }
    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, "Mesajınız Gönderildi, 10 İş Günü İçinde Dönüş Yapılacaktır")
            return redirect('home')
    else:
        messages.error(request, " Tüm Alanlar Zorunludur..!")
        form = ContactForm()
    context ={
        'form':form
    }
    return render(request, "contact.html", context)



def product_add(request):
    add = CreateForm()
    if request.method == 'POST':
        add = CreateForm(request.POST, request.FILES )
        if add.is_valid():
            add.save()
            messages.success(request, "Ürün Eklendi")
            return redirect('home')
        else:
            messages.error(request, "Birşeyler Yanlış Gitti Lütfen Tekrar Deneyin..")
    context = {
        'add':add
    }
    return render(request, "product-add.html", context)

def basket(request):
    return render(request, "basket.html")

        


