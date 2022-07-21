from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView,\
     UpdateView, DeleteView

from .models import *
from .forms import *


class IndexView(TemplateView):
    template_name = 'stdmanage/index.html'


class StudentCreateView(CreateView):
    form_class = StudentForm
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Student Record'
        return context


class StudentUpdateView(UpdateView):
    form_class = StudentForm 
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student Record'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('stdmanage:student-list')


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student_detail'


class ExamCreateView(CreateView):
    form_class = ExamForm
    model = Exam 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Exam Record'
        return context


class ExamUpdateView(UpdateView):
    form_class = ExamForm
    model = Exam 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Exam Record'
        return context


class ExamDeleteView(DeleteView):
    model = Exam
    success_url = reverse_lazy('stdmanage:exam-list')


class ExamDetailView(DetailView):
    model = Exam


class ExamListView(ListView):
    model = Exam


