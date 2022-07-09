from django.urls import path 
from . import views

app_name = 'stdmanage'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.add, name = 'add'),
    path('register', views.register, name= 'register'),
    path('show', views.show, name= 'show'),
]
