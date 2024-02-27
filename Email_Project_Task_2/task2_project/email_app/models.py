from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField()
    f_name = models.CharField(max_length = 45)
    l_name = models.CharField(max_length = 45)
    salary = models.FloatField()
    city = models.CharField(max_length = 45)
     
