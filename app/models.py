from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=50)
    Sprincipal=models.CharField(max_length=50)
    Slocation=models.CharField(max_length=50)

    def __str__(self):
        return self.Sname
    
class Student(models.Model):
    Stname=models.CharField(max_length=50)
    Sage=models.IntegerField()
    Sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.Stname