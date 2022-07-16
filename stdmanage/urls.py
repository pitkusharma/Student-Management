from django.urls import path 
from .views import *

app_name = 'stdmanage'
urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('student-create', StudentCreateView.as_view(), name = 'student-create'),
    path('student-list', StudentListView.as_view(), name = 'student-list'),
    
]