from django.db import models

# Create your models here.


# class Person(models.Model):
#     columns_list = ['survived','pclass','name','sex','age','sibsp','parch','ticket','fare']
#     def __init__(self,columns_list=columns_list, **kwargs):
#         for field in columns_list:
#             setattr(self, field, kwargs.get(field, None))


class Person(models.Model):
    survived = models.BooleanField()
    pclass = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=6)
    age = models.FloatField(null=True)
    sibsp = models.IntegerField(null=True)
    parch = models.IntegerField(null=True)
    ticket = models.CharField(max_length=20,null=True)
    fare = models.FloatField(null=True)

    def __str__(self):
        return self.name