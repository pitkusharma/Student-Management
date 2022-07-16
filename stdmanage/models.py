from django.db import models
from django.urls import reverse


class Student(models.Model):
    READING_CLASS_CHOICES = [
        ('eight', 'Eight'),
        ('nine', 'Nine'),
        ('ten', 'Ten'),
        ('eleven', 'Eleven'),
        ('tweleve', 'Tweleve')
    ]
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    full_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=10, default='male', choices=GENDER)
    date_of_birth = models.DateField(null=True, blank=True, )
    reading_class = models.CharField(max_length=20, choices=READING_CLASS_CHOICES )
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=200, null= True, blank=True, )

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.full_name
