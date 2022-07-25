from django.urls import path 
from .views import *

app_name = 'stdmanage'
urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),

    path('readingclass-create/', ReadingClassCreateView.as_view(), name = 'readingclass-create'),
    path('readingclass-update/<int:pk>/', ReadingClassUpdateView.as_view(), name = 'readingclass-update'),
    path('readingclass-delete/<int:pk>/', ReadingClassDeleteView.as_view(), name = 'readingclass-delete'),
    path('readingclass-list/', ReadingClassListView.as_view(), name = 'readingclass-list-basic'),
    path('readingclass-list/<int:row_limit>/<int:page_no>', 
        ReadingClassListView.as_view(), name = 'readingclass-list'),
    
    path('student-create/', StudentCreateView.as_view(), name = 'student-create'),
    path('student-update/<int:pk>/', StudentUpdateView.as_view(), name = 'student-update'),
    path('student-delete/<int:pk>/', StudentDeleteView.as_view(), name = 'student-delete'),
    path('student-detail/<int:pk>/', StudentDetailView.as_view(), name = 'student-detail'),
    path('student-list/<str:reading_class>/<int:row_limit>/<int:page_no>', 
        StudentListView.as_view(), name = 'student-list'),
    path('student-list/', StudentListView.as_view(), name = 'student-list-basic'),

    path('exam-create/', ExamCreateView.as_view(), name='exam-create'),
    path('exam-update/<int:pk>', ExamUpdateView.as_view(), name='exam-update'),
    path('exam-delete/<int:pk>', ExamDeleteView.as_view(), name='exam-delete'),
    path('exam-detail/<int:pk>', ExamDetailView.as_view(), name='exam-detail'),
    path('exam-list/<int:row_limit>/<int:page_no>/', ExamListView.as_view(), name='exam-list'),
    path('exam-list/', ExamListView.as_view(), name='exam-list-basic'),


    path('subject-create/', SubjectCreateView.as_view(), name = 'subject-create'),
    path('subject-update/<int:pk>/', SubjectUpdateView.as_view(), name = 'subject-update'),
    path('subject-delete/<int:pk>/', SubjectDeleteView.as_view(), name = 'subject-delete'),
    path('subject-list/', SubjectListView.as_view(), name = 'subject-list-basic'),
    path('subject-list/<int:row_limit>/<int:page_no>', 
        SubjectListView.as_view(), name = 'subject-list'),

    
    path('result-add-list/', ResultAddListView.as_view(), name='result-add-list-basic'),
    path('result-add-list/<str:exam>/<str:subject>/<str:reading_class>/<int:row_limit>/<int:page_no>/', 
        ResultAddListView.as_view(), name='result-add-list'),

    path('result-create/', ResultCreateView.as_view(), name='result-create-basic'),
    path('result-create/<str:exam>/<str:subject>/<int:student>', ResultCreateView.as_view(), name='result-create'),

    
]