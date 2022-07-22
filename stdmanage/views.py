import math
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView,\
     UpdateView, DeleteView
from matplotlib.pyplot import get

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


class StudentListView(View):
    template_name = 'stdmanage/student_list.html'
    
    def get(self, request, *args, **kwargs):
    #<str:reading_class>/<int:row_limit>/<int:page_no>    
        if kwargs['reading_class'] == 'all':
            student_list = Student.objects.all()  
            reading_class = kwargs['reading_class']
        else:
            reading_class = kwargs['reading_class']
            reading_class_id = ReadingClass.objects.get(name = reading_class).id
            student_list = Student.objects.filter(reading_class = reading_class_id)

        row_limit = kwargs['row_limit']
        page_no = kwargs['page_no'] # because page no. starts from zero

        context = {}

        context['student_list'] = student_list[ ( page_no - 1 ) * row_limit : page_no * row_limit ] 
      
        context['assign_page_no'] = [i+1 for i in range # to provide an iterable in panigation
            ( 0, math.floor( ( student_list.count()  / row_limit ) + 1 ) ) ]

        if page_no == context['assign_page_no'][0]:    
            print(context['assign_page_no'][0], page_no)
            context['prev_current_next'] = ( context['assign_page_no'][0], page_no, page_no+1 )
        
        elif page_no == context['assign_page_no'][-1]:
            context['prev_current_next'] = ( page_no-1, page_no, context['assign_page_no'][-1] )
        
        else:
            context['prev_current_next'] = ( page_no-1, page_no, page_no+1 )

        context['reading_class'] = reading_class
        
        context['row_limit'] = row_limit

        context['all_reading_class'] = ReadingClass.objects.all()
        
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        
        reading_class = request.POST['reading_class']
        row_limit = request.POST['row_limit']

        return HttpResponseRedirect(reverse('stdmanage:student-list', 
            kwargs={'reading_class': reading_class, 
                'row_limit': row_limit,
                'page_no': 1
            }))

    # def get_context_data(self, **kwargs):
        
    #     context = super().get_context_data(**kwargs) 
        
    #     if self.kwargs['reading_class'] == 'all':
    #         student_list = Student.objects.all()
        
    #     elif self.kwargs['reading_class'] == 'set':
    #         pass
    #     else:
    #         pass

        
    #     return context 
        
        # if self.kwargs['reading_class'] == 'all':
            
        #     reading_class_is = self.kwargs['reading_class']
        #     student_list = Student.objects.all()
        #     row_limit = self.kwargs['row_limit']
        
        # elif self.kwargs['reading_class'] == 'set':

        #     return HttpResponseRedirect(reverse('student-list'))
            
        #     reading_class_is = self.request.GET['reading_class']
            
        #     reading_class_id = ReadingClass.objects.get(name = reading_class_is).id
        #     student_list = Student.objects.filter(reading_class = reading_class_id)
            
        #     row_limit = int(self.request.GET['row_limit'])
            
        # else:
            
        #     reading_class_is = self.kwargs['reading_class']
        #     reading_class_id = ReadingClass.objects.get(name = reading_class_is).id
        #     student_list = Student.objects.filter(reading_class = reading_class_id)
        #     row_limit = self.kwargs['row_limit']

        # page_no = self.kwargs['page_no']
               
        # #returing the sliced list
        # context['student_list'] = student_list[(page_no-1)*row_limit : page_no*row_limit] 

        # context['assign_page_no'] = [i+1 for i in range #to provide an iterable in panigation
        #     (0, math.ceil((student_list.count())/row_limit))]

        # if page_no == context['assign_page_no'][0]:    
        #     context['prev_current_next'] = (context['assign_page_no'][0], page_no, page_no+1)
        
        # elif page_no == context['assign_page_no'][-1]:
        #     context['prev_current_next'] = (page_no-1, page_no, context['assign_page_no'][-1])
        
        # else:
        #     context['prev_current_next'] = (page_no-1, page_no, page_no+1)

        # context['reading_class'] = reading_class_is
        
        # context['row_limit'] = row_limit

        # context['all_reading_class'] = ReadingClass.objects.all()
        
        # return context


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


