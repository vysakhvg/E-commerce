from . import views
from django.urls import path
app_name='shopapp'

urlpatterns = [
    path('',views.Allprocat,name='Allprocat'),
    path('<slug:c_slug>/',views.Allprocat,name='products_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='productdeatil'),
]