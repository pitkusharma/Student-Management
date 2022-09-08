from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import *
from .forms import *


class IndexView(generic.View):
    template_name = 'stdmanage/index.html'

    def get(self,request, *args, **kwargs):
        context = {}
        context["student_count"] = Student.objects.all().count()
        context["recent_students"] = Student.objects.all()[:5]
        context["recent_exams"] = Exam.objects.all()[:3]
        context["recent_result"] = Result.objects.all()[:5]

        return render(request, self.template_name, context)



class StudentCreateView(generic.CreateView):
    template_name = 'stdmanage/form.html'
    form_class = StudentForm
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Student Record'
        context['submit_text'] = 'Create Student'
        return context


class StudentUpdateView(generic.UpdateView):
    template_name = 'stdmanage/form.html'
    form_class = StudentForm 
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student Record'
        context['submit_text'] = 'Update Student'
        return context


class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('stdmanage:student-list', kwargs={'page_no': 1})
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete student " + the_object.full_name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:student-delete'
        context['go_back_url'] = reverse('stdmanage:student-detail', kwargs={'pk': the_object.id})
        return context


class StudentListView(generic.View):
    template_name = "stdmanage/student_list.html"
    
    def get_list(self,request, *args, **kwargs):
        context = {}
        
        context['all_class'] = ReadingClass.objects.all()
        
        try:
            context["reading_class"] = request.session["reading_class"]
        except:
            context["reading_class"] = "all"
            request.session["reading_class"] = "all"
        
        if context["reading_class"] != "all":
            reading_class = ReadingClass.objects.get(name = request.session["reading_class"])
            student_list = Student.objects.filter(reading_class = reading_class)
        else:
            student_list = Student.objects.all()
        
        return [context, student_list]

    def get(self, request, *args, **kwargs):
        res = self.get_list(request, *args, **kwargs)
        context = res[0]
        list_object = res[1]

        try:
            page_size = int(request.session["page_size"])
        except:
            page_size = 5
            request.session["page_size"] = page_size
        context["page_size"] = page_size

        try:
            page_no = kwargs["page_no"]
        except:
            page_no = 1

        context["list_object"] = list_object[ ( page_no - 1 ) * page_size : page_no * page_size ]
        
        count = len(list_object)
        i = 1
        pages = []
        while count >= 0:
            pages.append(i)
            i += 1
            count -= page_size

        context["pages"] = pages
        context["current"] = page_no

        if page_no != pages[0]:
            context["prev"] = page_no - 1
        else:
            context["prev"] = 1

        if page_no != pages[-1]:
            context["next"] = page_no + 1
        else:
            context["next"] = pages[-1]

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            request.session["reading_class"] = request.POST["reading_class"]
        except:
            pass
        try:
            request.session["page_size"] = request.POST["page_size"]
        except:
            pass
        
        return HttpResponseRedirect(reverse("stdmanage:student-list", kwargs={
            "page_no": 1
        }))


class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student_detail'


class ReadingClassCreateView(generic.CreateView):
    template_name = 'stdmanage/form.html'
    model = ReadingClass
    form_class = ReadingClassForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Reading Class'
        context['submit_text'] = 'Create'
        return context


class ReadingClassUpdateView(generic.UpdateView):
    template_name = 'stdmanage/form.html'
    model = ReadingClass
    form_class = ReadingClassForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Reading Class'
        context['submit_text'] = 'Update'
        return context


class ReadingClassDeleteView(generic.DeleteView):
    model = ReadingClass
    success_url = reverse_lazy("stdmanage:readingclass-list", kwargs = {"page_no": 1})
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete class " + the_object.name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:readingclass-delete'
        context['go_back_url'] = reverse('stdmanage:readingclass-list', kwargs={"page_no": 1})
        return context


class ReadingClassListView(StudentListView):
    template_name = 'stdmanage/readingclass_list.html'
    
    def get_list(self, request, *args, **kwargs):
        context = {}
        all_class = ReadingClass.objects.all()
        return context, all_class
    
    def post(self, request, *args, **kwargs):
        try:
            request.session["page_size"] = request.POST["page_size"]
        except:
            pass
        
        return HttpResponseRedirect(reverse("stdmanage:readingclass-list", kwargs={
            "page_no": 1
        }))


class SubjectCreateView(generic.CreateView):
    template_name = 'stdmanage/form.html'
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Teaching Subject'
        context['submit_text'] = 'Create'
        return context


class SubjectUpdateView(generic.UpdateView):
    template_name = 'stdmanage/form.html'
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Subject'
        context['submit_text'] = 'Update'
        return context


class SubjectDeleteView(generic.DeleteView):
    model = Subject
    success_url = reverse_lazy("stdmanage:subject-list", kwargs={'page_no': 1})
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete subject " + the_object.name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:subject-delete'
        context['go_back_url'] = reverse('stdmanage:subject-list', kwargs={"page_no": 1})
        return context


class SubjectListView(StudentListView):
    template_name = 'stdmanage/subject_list.html'
    
    def get_list(self, request, *args, **kwargs):
        context = {}    
        all_subjects = Subject.objects.all()
        return context, all_subjects
    
    def post(self, request, *args, **kwargs):
        try:
            request.session["page_size"] = request.POST["page_size"]
        except:
            pass
        
        return HttpResponseRedirect(reverse("stdmanage:subject-list", kwargs={
            "page_no": 1
        }))


class ExamCreateView(generic.CreateView):
    template_name = 'stdmanage/form.html'
    form_class = ExamForm
    model = Exam 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Exam Record'
        context['submit_text'] = 'Create Exam'
        return context


class ExamUpdateView(generic.UpdateView):
    template_name = 'stdmanage/form.html'
    form_class = ExamForm
    model = Exam 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Exam Record'
        context['submit_text'] = 'Update Exam'
        return context


class ExamDeleteView(generic.DeleteView):
    model = Exam
    success_url = reverse_lazy('stdmanage:exam-list', kwargs={'page_no': 1})
    template_name = 'stdmanage/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete exam " + the_object.name + " ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:exam-delete'
        context['go_back_url'] = reverse('stdmanage:exam-detail', kwargs={'pk': the_object.id})
        return context


class ExamDetailView(generic.DetailView):
    model = Exam


class ExamListView(StudentListView):
    template_name = 'stdmanage/exam_list.html'

    def get_list(self, request, *args, **kwargs):
        context = {}        
        exam_list = Exam.objects.all()

        return [context, exam_list]
    
    def post(self, request, *args, **kwargs):
        try:
            request.session["page_size"] = request.POST["page_size"]
        except:
            pass
        
        return HttpResponseRedirect(reverse("stdmanage:exam-list", kwargs={
            "page_no": 1
        }))


class ResultAddListView(StudentListView):
    template_name = 'stdmanage/result_add_list.html'
    
    def get_list(self, request, *args, **kwargs):
        context = {}        
        
        try:
            subject = Subject.objects.get(name = request.session["subject"])
        except:
            subject = Subject.objects.all().first()
        context["subject"] = subject.name
        
        try:
            reading_class = ReadingClass.objects.get(name = request.session["reading_class"])
        except:
            reading_class = ReadingClass.objects.all().first()
        context["reading_class"] = reading_class.name
        
        
        try:
            exam = Exam.objects.get(name = request.session["exam"])
        except:
            exam = Exam.objects.all().first()
        context["exam"] = exam.name

        result_list = Student.objects.all()
        if reading_class != "all":
            temp = []
            for i in result_list:
                if i.reading_class == reading_class:
                    result = Result.objects.filter(
                        exam = exam,
                        subject = subject,
                        student = i
                    )
                    if result.count() == 0:
                        temp.append(i)

            result_list = temp
        
        context["all_exams"] = Exam.objects.all()
        context["all_subjects"] = Subject.objects.all()
        context["all_class"] = ReadingClass.objects.all()
        return [context, result_list]
    
    def post(self, request, *args, **kwargs):
        try:
            request.session["page_size"] = request.POST["page_size"]
        except:
            pass
        try:
            request.session["subject"] = request.POST["subject"]
        except:
            pass
        try:
            request.session["reading_class"] = request.POST["reading_class"]
        except:
            pass
        try:
            request.session["exam"] = request.POST["exam"]
        except:
            pass
        
        return HttpResponseRedirect(reverse("stdmanage:result-add-list", kwargs={
            "page_no": 1
        }))


class ResultCreateView(generic.FormView):
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

            return HttpResponse("Record Saved")
        
        else:
            context = {}
            context['form'] = form_data

            return render(request, self.template_name, context)


class ResultListView(StudentListView):
    template_name = "stdmanage/result_list.html"

    def get_list(self, request, *args, **kwargs):
        context = {}        
        
        try:
            subject = Subject.objects.get(name = request.session["subject"])
        except:
            subject = Subject.objects.all().first()
        context["subject"] = subject.name
        
        try:
            reading_class = ReadingClass.objects.get(name = request.session["reading_class"])
        except:
            reading_class = ReadingClass.objects.all().first()
        context["reading_class"] = reading_class.name
        
        
        try:
            exam = Exam.objects.get(name = request.session["exam"])
        except:
            exam = Exam.objects.all().first()
        context["exam"] = exam.name

        result_list = Result.objects.filter(
            exam = exam,
            subject = subject,
        )
        
        temp = []
        for i in result_list:
            if i.student.reading_class == reading_class:
                temp.append(i)
        result_list = temp
        
        context["all_exams"] = Exam.objects.all()
        context["all_subjects"] = Subject.objects.all()
        context["all_class"] = ReadingClass.objects.all()
        return [context, result_list]
    
    def post(self, request, *args, **kwargs):
        try:
            request.session["page_size"] = request.POST["page_size"]
        except:
            pass
        try:
            request.session["subject"] = request.POST["subject"]
        except:
            pass
        try:
            request.session["reading_class"] = request.POST["reading_class"]
        except:
            pass
        try:
            request.session["exam"] = request.POST["exam"]
        except:
            pass
        
        return HttpResponseRedirect(reverse("stdmanage:result-list", kwargs={
            "page_no": 1
        }))


class ResultUpdateView(generic.UpdateView):
    template_name = 'stdmanage/form.html'
    form_class = ResultForm
    model = Result
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Record'
        context['submit_text'] = 'Update'
        return context


class ResultDeleteView(generic.DeleteView):
    template_name = 'stdmanage/confirm_delete.html'
    model = Result
    success_url = reverse_lazy('stdmanage:result-list', kwargs = {
        "page_no": 1
    })
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_object = self.model.objects.get(id = self.kwargs['pk'])
        title = "Are you sure you want to delete " + the_object.student.full_name + " result ?" 
        context['title'] = title
        context['delete_url_name'] = 'stdmanage:result-delete'
        context['go_back_url'] = reverse('stdmanage:result-list', kwargs = {
            "page_no": 1
            })
        return context



