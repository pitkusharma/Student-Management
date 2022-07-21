from django.urls import path 
from .views import *

app_name = 'stdmanage'
urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    
    path('student-create/', StudentCreateView.as_view(), name = 'student-create'),
    path('student-update/<int:pk>/', StudentUpdateView.as_view(), name = 'student-update'),
    path('student-delete/<int:pk>/', StudentDeleteView.as_view(), name = 'student-delete'),
    path('student-detail/<int:pk>/', StudentDetailView.as_view(), name = 'student-detail'),
    path('student-list/', StudentListView.as_view(), name = 'student-list'),

    path('exam-create/', ExamCreateView.as_view(), name='exam-create'),
    path('exam-update/<int:pk>', ExamUpdateView.as_view(), name='exam-update'),
    path('exam-delete/<int:pk>', ExamDeleteView.as_view(), name='exam-delete'),
    path('exam-detail/<int:pk>', ExamDetailView.as_view(), name='exam-detail'),
    path('exam-list/', ExamListView.as_view(), name='exam-list'),
    
]