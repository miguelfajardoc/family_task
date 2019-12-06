from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('create data')
    update_date = models.DateTimeField('Update data')

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    creation_date = models.DateTimeField('create date')
    update_date = models.DateTimeField('update date')
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

class Task(models.Model):
    name = models.CharField(max_length=200)
    time = models.IntegerField(default=0)
    frequency = models.CharField(max_length=200)
    status = models.CharField(max_length=10)
    creation_date = models.DateTimeField('create data')
    update_date = models.DateTimeField('Update data')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
