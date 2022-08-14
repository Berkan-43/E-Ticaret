from django.shortcuts import render
from favories.models import *

# Create your views here.
def favori(request):
    urun2 = Urunler.objects.all()
     # Search
    search_product = ''
    if request.GET.get('search_product'):
        search_product = request.GET.get('search_product')
        urun2 = urun2.filter(hakkinda__icontains = search_product)
    context = {
        'urun':urun2,
        'search_product':search_product
    }
    return render(request, 'favories.html', context)

