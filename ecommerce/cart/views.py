from django.shortcuts import render, redirect
from cart.models import Cart, Account, Order
from shop.models import Category, Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def cart_view(request):
    total = 0
    try:
        user = request.user
        cart = Cart.objects.filter(user=user)
        for i in cart:
            total += i.quantity * i.products.price
    except Cart.DoesNotExists:
        pass
    return render(request, 'cart.html', {'cart': cart, 'total': total})


@login_required
def cartpg(request, p):
    prod = Product.objects.get(id=p)
    user = request.user
    try:
        cart = Cart.objects.get(products=prod, user=user)
        if cart.quantity < cart.products.stock:
            cart.quantity += 1
        cart.save()
    except Cart.DoesNotExist:
        cart = Cart.objects.create(products=prod, user=user, quantity=1)
        cart.save()
    return redirect('cart:cart_view')


@login_required
def item_reduce(request, p):
    user = request.user
    prod = Product.objects.get(id=p)
    try:
        cart = Cart.objects.get(user=user, products=prod)
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()

    except:
        pass
    return redirect('cart:cart_view')


@login_required
def item_remove(request, id):
    user = request.user
    prod = Product.objects.get(id=id)
    try:
        cart = Cart.objects.get(user=user, products=prod)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')


@login_required
def porder(request):
    total = 0
    items = 0
    if request.method == "POST":
        address = request.POST['add']
        phnnum = request.POST['phn']
        accnum = request.POST['accnum']
        user = request.user
        # o = Order.objects.create(address=address, phone=phnnum, user=user)
        cart = Cart.objects.filter(user=user)
        for i in cart:
            total += i.quantity * i.products.price
            items += i.quantity
        acc = Account.objects.get(accnumber=accnum)
        if float(acc.amount) >= total:
            acc.amount = acc.amount - total
            acc.save()
            for i in cart:
                o = Order.objects.create(user=user, products=i.products, address=address, phone=phnnum,
                                         order_status="paid",
                                         noofitems=i.quantity)
                o.save()
            cart.delete()
            msg = "Order placed successfully"
            return render(request, 'orderdetails.html', {'msg': msg, 'total': total, 'items': items})
        else:
            msg = "Insufficient amount"
            return render(request, 'orderdetails.html', {'msg': msg})

    return render(request, 'order.html')


def yourorder(request):
    user = request.user
    order = Order.objects.filter(user=user, order_status="paid")
    return render(request, 'orderview.html', {'ord': order, 'name': user.username})
