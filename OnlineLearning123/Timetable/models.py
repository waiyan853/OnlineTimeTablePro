from django.db import models

# Create your models here.
class RegisterationData(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField(max_length=50)
    major=models.CharField(max_length=100)
    rollno=models.IntegerField(max_length=50)
    def __str__(self):
        return self.name