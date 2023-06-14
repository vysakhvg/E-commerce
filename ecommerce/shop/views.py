from django.shortcuts import render
from shop.models import Category, Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def allProcat(request):
    categry = Category.objects.all()
    return render(request, 'category.html', {'c': categry})


def allproduct(request, slug):
    cat = Category.objects.get(slug=slug)
    products = Product.objects.filter(category__slug=slug)
    return render(request, 'product.html', {'p': products, 'c': cat})


def prodetail(request, slug):
    pro = Product.objects.get(slug=slug)
    return render(request, 'detail.html', {'p': pro})


def signup(request):
    if request.method == 'POST':
        u = request.POST['usr']
        fn = request.POST['fname']
        ln = request.POST['lname']
        m = request.POST['mail']
        p = request.POST['pass']
        cp = request.POST['cpass']
        if p == cp:
            user = User.objects.create_user(username=u, first_name=fn, last_name=ln, email=m, password=p)
            user.save()
            return allProcat(request)
        else:
            print('Password Incorrect')
    return render(request, 'signup.html')


def ulogin(request):
    if request.method == 'POST':
        u = request.POST['us']
        p = request.POST['pas']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return allProcat(request)
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')


def ulogout(request):
    logout(request)
    return allProcat(request)
