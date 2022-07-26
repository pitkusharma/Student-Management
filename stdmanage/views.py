import math
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView,\
     UpdateView, DeleteView

from .models import *
from .forms import *


class IndexView(TemplateView):
    template_name = 'stdmanage/index.html'


class StudentCreateView(CreateView):
    template_name = 'stdmanage/create_update_form.html'
    form_class = StudentForm
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Student Record'
        context['submit_text'] = 'Create Student'
        return context


class StudentUpdateView(UpdateView):
    template_name = 'stdmanage/create_update_form.html'
    form_class = StudentForm 
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student Record'
        context['submit_text'] = 'Update Student'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('stdmanage:student-list-basic')
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete student " + the_object.full_name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:student-delete'
        context['go_back_url'] = reverse('stdmanage:student-detail', kwargs={'pk': the_object.id})
        return context


class StudentListView(View):
    template_name = 'stdmanage/student_list.html'
    pagination_url = 'stdmanage:student-list'
    list_object_name = 'student_list'
    model = Student
    exam_use = False
    subject_use = False
    class_use = True
    
    def get(self, request, *args, **kwargs):
        
        context = {}
        list_object = self.model.objects.all()

        if self.class_use == True:

            try:
                if kwargs['reading_class'] == 'all':
                    list_object = self.model.objects.all()  
                    reading_class = kwargs['reading_class']
                
                else:
                    reading_class = kwargs['reading_class']
                    reading_class_id = ReadingClass.objects.get(name = reading_class).id
                    list_object = self.model.objects.filter(reading_class = reading_class_id)
            
            except:
                reading_class = 'all'
                list_object = self.model.objects.all()

            context['reading_class'] = reading_class
            context['all_reading_class'] = ReadingClass.objects.all()

        if self.subject_use == True:
            
            try:
                subject  = kwargs['subject']
            except:
                subject = 'select subject'
            
            context['subject'] = subject
            context['all_subjects'] = Subject.objects.all()
        
        if self.exam_use == True:
            
            try:
                subject  = kwargs['exam']
            except:
                subject = 'select exam'
            
            context['exam'] = subject
            context['all_exams'] = Exam.objects.all()
        
        try:
            row_limit = kwargs['row_limit']
        except:
            row_limit = 5
        
        try:   
            page_no = kwargs['page_no'] # because page no. starts from zero
        except:
            page_no = 1

        context[self.list_object_name] = list_object[ ( page_no - 1 ) * row_limit : page_no * row_limit ] 
      
        context['assign_page_no'] = [i+1 for i in range # to provide an iterable in panigation
            ( 0, math.floor( ( list_object.count()  / row_limit ) + 1 ) ) ]

        if page_no == context['assign_page_no'][0]:    
            
            print(context['assign_page_no'][0], page_no)
            context['prev_current_next'] = ( context['assign_page_no'][0], page_no, page_no+1 )
        
        elif page_no == context['assign_page_no'][-1] or page_no > context['assign_page_no'][-1]:
            
            context['prev_current_next'] = ( page_no-1, page_no, context['assign_page_no'][-1] )
        
        else:
            
            context['prev_current_next'] = ( page_no-1, page_no, page_no+1 )

        context['row_limit'] = row_limit
        
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        kwargs_dict = {}

        if self.exam_use == True:
            exam = request.POST['exam']
            kwargs_dict['exam'] = exam

        if self.subject_use == True:
            subject = request.POST['subject']
            kwargs_dict['subject'] = subject

        if self.class_use == True:
            reading_class = request.POST['reading_class']
            kwargs_dict['reading_class'] = reading_class

        row_limit = request.POST['row_limit']
        
        kwargs_dict['row_limit'] = row_limit
        kwargs_dict['page_no'] = 1        

        return HttpResponseRedirect(reverse(self.pagination_url, kwargs= kwargs_dict))


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student_detail'


class ExamCreateView(CreateView):
    template_name = 'stdmanage/create_update_form.html'
    form_class = ExamForm
    model = Exam 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Exam Record'
        context['submit_text'] = 'Create Exam'
        return context


class ExamUpdateView(UpdateView):
    template_name = 'stdmanage/create_update_form.html'
    form_class = ExamForm
    model = Exam 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Exam Record'
        context['submit_text'] = 'Update Exam'
        return context


class ExamDeleteView(DeleteView):
    model = Exam
    success_url = reverse_lazy('stdmanage:exam-list-basic')
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete exam " + the_object.name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:exam-delete'
        context['go_back_url'] = reverse('stdmanage:exam-detail', kwargs={'pk': the_object.id})
        return context


class ExamDetailView(DetailView):
    model = Exam


class ExamListView(StudentListView):
    template_name = 'stdmanage/exam_list.html'
    pagination_url = 'stdmanage:exam-list'
    list_object_name = 'exam_list'
    model = Exam
    exam_use = False
    subject_use = False
    class_use = False


class ResultAddListView(StudentListView):
    template_name = 'stdmanage/result_add_list.html'
    pagination_url = 'stdmanage:result-add-list'
    list_object_name = 'student_list'
    model = Student
    exam_use = True
    subject_use = True
    class_use = True


class ResultCreateView(FormView):
    template_name = 'stdmanage/result_form.html'
    model = Result
    form_class = ResultForm

    def get(self, request, *args, **kwargs):
        
        context = {}
        form_data = {}
        try:
            exam = kwargs['exam']
            exam_id = Exam.objects.get(name=exam).id
            form_data['exam'] = exam_id
        except:
            exam = 'none'
        
        try:
            subject = kwargs['subject']
            subject_id = Subject.objects.get(name=subject).id
            form_data['subject'] = subject_id
        except:
            subject = 'none'
        
        try:
            student = kwargs['student']
            student_id = Student.objects.get(id=student).id
            form_data['student'] = student_id
        except:
            student = 'none'

        result_form = self.form_class(initial = form_data)
        
        context['form'] = result_form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        form_data = self.form_class(request.POST, request.FILES)
        
        if form_data.is_valid():
            form_data.save()

            return HttpResponse("Form Data Saved")
        
        else:
            context = {}
            context['form'] = form_data

            return render(request, self.template_name, context)


class ReadingClassCreateView(CreateView):
    template_name = 'stdmanage/create_update_form.html'
    model = ReadingClass
    form_class = ReadingClassForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Reading Class'
        context['submit_text'] = 'Create'
        return context


class ReadingClassUpdateView(UpdateView):
    template_name = 'stdmanage/create_update_form.html'
    model = ReadingClass
    form_class = ReadingClassForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Reading Class'
        context['submit_text'] = 'Update'
        return context


class ReadingClassDeleteView(DeleteView):
    model = ReadingClass
    success_url = reverse_lazy("stdmanage:readingclass-list-basic")
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete class " + the_object.name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:readingclass-delete'
        context['go_back_url'] = reverse('stdmanage:readingclass-list-basic', kwargs={})
        return context


class ReadingClassListView(StudentListView):
    template_name = 'stdmanage/readingclass_list.html'
    pagination_url = 'stdmanage:readingclass-list'
    list_object_name = 'class_list'
    model = ReadingClass
    exam_use = False
    subject_use = False
    class_use = False






class SubjectCreateView(CreateView):
    template_name = 'stdmanage/create_update_form.html'
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Teaching Subject'
        context['submit_text'] = 'Create'
        return context


class SubjectUpdateView(UpdateView):
    template_name = 'stdmanage/create_update_form.html'
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Subject'
        context['submit_text'] = 'Update'
        return context


class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy("stdmanage:subject-list-basic")
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete subject " + the_object.name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:subject-delete'
        context['go_back_url'] = reverse('stdmanage:subject-list-basic', kwargs={})
        return context

class SubjectListView(StudentListView):
    template_name = 'stdmanage/subject_list.html'
    pagination_url = 'stdmanage:subject-list'
    list_object_name = 'subject_list'
    model = Subject
    exam_use = False
    subject_use = False
    class_use = False