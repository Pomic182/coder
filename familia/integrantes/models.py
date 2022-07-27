from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=40)    
    creation_date = models.DateField(auto_now_add=True)
    edad = models.IntegerField()