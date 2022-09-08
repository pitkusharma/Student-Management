from django.db import models
from django.urls import reverse


class ReadingClass(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stdmanage:readingclass-list", kwargs={"page_no": 1})


class Student(models.Model):
      
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    full_name = models.CharField(
        max_length=60
        )
    gender = models.CharField(
        max_length=10, 
        default='male', 
        choices=GENDER
        )
    date_of_birth = models.DateField(
        null=True, 
        blank=True, 
        )
    reading_class = models.ForeignKey(
        ReadingClass, 
        on_delete=models.CASCADE
        )
    phone_number = models.CharField(
        max_length=20
        )
    home_address = models.CharField(
        max_length=200, 
        null= True, 
        blank=True, 
        )
    photo = models.FileField(
        upload_to='student_photos', 
        null=True
        )

    def get_absolute_url(self):
        return reverse('stdmanage:student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.full_name


class Exam(models.Model):
    
    name = models.CharField(
        max_length=50
        )
    description = models.CharField(
        max_length=200
        )
    date = models.DateField()
    question_papers = models.FileField(
        upload_to='question_papers',  
        )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stdmanage:exam-detail", kwargs={"pk": self.pk})


class Subject(models.Model):

    name = models.CharField(
        max_length=20
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stdmanage:subject-list", kwargs={"page_no": 1})


class Result(models.Model):

    score = models.CharField(
        max_length=10
        )
    answer_sheet = models.FileField(
        upload_to='answer_sheets'
        )
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE
        )
    subject = models.ForeignKey(
        Subject, 
        on_delete=models.CASCADE
        )
    exam = models.ForeignKey(
        Exam, 
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return self.student.full_name + "'s score"

    def get_absolute_url(self):
        return reverse("stdmanage:result-list", kwargs={"page_no": 1})
