from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField()
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField()
    adress = models.TextField()
    
