from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


# Create your views here.

def srchrslt(request):
    products = None
    srch = ''
    if request.method == 'POST':
        srch = request.POST['sear']
        if srch:
            products = Product.objects.filter(Q(name__icontains=srch) | Q(description__icontains=srch))
    return render(request, 'search.html', {'s': srch, 'p': products})
