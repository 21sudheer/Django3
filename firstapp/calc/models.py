from django.db import models

# Create your models here.
        
class Employee(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone_number=models.IntegerField(null = True)
    Email=models.EmailField(max_length=200)
    salary = models.FloatField(null=True)
    
    def __str__(self):
        return self.first_name