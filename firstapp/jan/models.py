from django.db import models

# Create your models here.
class Application(models.Model):
    NAME = models.CharField(max_length=255)
    Email = models.EmailField(null=True)
    Salary= models.FloatField(null=True)
    def __str__(self):
        return self.NAME
