from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    def __str__(self):
        return f'ID: {self.id}, Username: {self.username}, Email: {self.email}, First Name: {self.first_name}, Last Name: {self.last_name}'


class Posts(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    date = models.DateTimeField()
    post = models.TextField(null=False)

    def serialize(self):
        return {"First Name": self.first_name}
    
    def __str__(self):
        return f'ID: {self.id} First: {self.first_name}, Last: {self.last_name}, username: {self.username}, Date: {self.date}, Post: {self.post}'

    

