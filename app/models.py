from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('create date')
    update_date = models.DateTimeField('update date')

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    creation_date = models.DateTimeField('create date')
    update_date = models.DateTimeField('update date')
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def name_spc(self):
        return list(self.name)

class Task(models.Model):
    name = models.CharField(max_length=200)
    time = models.IntegerField(default=0)
    frequency = models.CharField(max_length=200)
    status = models.CharField(max_length=10)
    creation_date = models.DateTimeField('create date')
    update_date = models.DateTimeField('Update date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
