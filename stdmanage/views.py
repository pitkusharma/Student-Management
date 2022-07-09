from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import datetime

from .models import Student


def index(request):
  context = {
    'var1': 'Fuck you' 
  }
  return render(request, 'stdmanage/index.html', context)

def add(request):
  context = {
  }
  return render(request, 'stdmanage/add.html', context)

def register(request):
  full_name = request.POST['fullName']
  date_of_birth = request.POST['dateOfBirth']
  date_obj = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
  select_class = request.POST['selectClass']
  ph_number = request.POST['phNumber']
  home_address = request.POST['homeAddress']

  student = Student(fullName = full_name, dateOfBirth = date_obj, selectClass = select_class, phNumber = ph_number, homeAddress = home_address)
  student.save()

  return HttpResponseRedirect(reverse('stdmanage:add'))

def show(request):
  allStudents = Student.objects.all()
  context = {
    'allStudents': allStudents,
  }
  return render(request, "stdmanage/show.html", context)
