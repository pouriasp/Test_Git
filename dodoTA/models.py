from django.db import models

# Create your models here.
class havijpolomorgh(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    birthday=models.DateTimeField()