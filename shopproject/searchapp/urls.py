from . import views
from django.urls import path

app_name='searchapp'

urlpatterns = [
    path('',views.search_result,name='search_result'),
]