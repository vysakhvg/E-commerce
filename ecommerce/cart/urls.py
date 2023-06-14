from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('<int:p>', views.cartpg, name='cartpg'),
    path('cview/', views.cart_view, name='cart_view'),
    path('cminus/<int:p>', views.item_reduce, name='item_reduce'),
    path('iremove/<int:id>', views.item_remove, name='item_remove'),
    path('porder', views.porder, name='porder'),
    path('yourorder', views.yourorder, name='yourorder'),
]
