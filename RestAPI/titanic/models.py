from django.db import models

# Create your models here.

class Person(models.Model):
    survived = models.BooleanField()
    pclass = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=6, null=True)
    age = models.FloatField(null=True)
    sibsp = models.IntegerField(null=True)
    parch = models.IntegerField(null=True)
    ticket = models.CharField(max_length=20,null=True)
    fare = models.FloatField(null=True)

    def __str__(self):
        return self.name
    
