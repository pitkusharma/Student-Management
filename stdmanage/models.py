from django.db import models

class Student(models.Model):
  fullName = models.CharField(max_length=60, null= True)
  dateOfBirth = models.DateField(null=True)
  selectClass = models.CharField(max_length=20, null= True)
  phNumber = models.CharField(max_length=15, null= True)
  homeAddress = models.CharField(max_length=200, null= True)

  # def __str__(self):
  #   return self.fullName
