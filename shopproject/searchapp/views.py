from django.shortcuts import render
from shopapp.models import product
from django.db.models import Q
# Create your views here.

def search_result(request):
    products=None
    Query=None
    if 'q' in request.GET:
        Query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=Query) | Q(description__contains=Query))
        return render(request,'search.html',{'query':Query,'products':products})
