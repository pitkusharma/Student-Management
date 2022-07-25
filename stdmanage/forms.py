from django import forms

from .models import *


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        YEARS = {
            '1999':'1999',
            '2001':'2001',
            '2002':'2002',
            '2003':'2003',
            '2004':'2004',
            '2005':'2005',
            '2006':'2006',
            '2007':'2007',
            '2008':'2008',
            '2009':'2009',
            '2010':'2010',
        }
        widgets = {
            'date_of_birth': forms.DateInput( attrs={'type': 'date',} ),
            'home_address': forms.Textarea( attrs={'cols': '20', 'rows': '5'} ),
        }
        labels = {
            'full_name': 'Enter full name of the student',
        }
        help_texts = {

        }
        error_messages = {

        }


class ExamForm(forms.ModelForm):
    
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget,
            'description': forms.Textarea(attrs={'rows': '5'})
        }


class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = '__all__'
   
