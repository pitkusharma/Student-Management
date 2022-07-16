from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView

from .models import Student
from .forms import StudentForm


class IndexView(TemplateView):
    template_name = 'stdmanage/index.html'


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    template_name = 'stdmanage/student_create.html'
    form_class = StudentForm
    success_url = "student-create"
    model = Student
