from django.urls import path
from shop import views
app_name = 'shop'

urlpatterns = [
    path('', views.allProcat, name='allProcat'),
    path('product/<slug:slug>', views.allproduct, name='allproduct'),
    path('detail/<slug:slug>', views.prodetail, name='prodetail'),
    path('signup', views.signup, name='signup'),
    path('ulogin', views.ulogin, name='ulogin'),
    path('ulogout', views.ulogout, name='ulogout'),
]
