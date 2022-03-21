from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    occupants_count = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hood_name


class Business(models.Model):
    business = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.business


class Post(models.Model):
    title = models.CharField(max_length=30)
    post = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Contact(models.Model):
    emergency_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


    def __str__(self):
        return self.emergency_name


