import datetime

from django.db import models

from users.models import Patient


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.task} - {self.patient}'


class Article(models.Model):
    pictures = models.ImageField(upload_to="images/", blank=True, null=True)
    title = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return self.title


class Handbook(models.Model):
    week = models.PositiveSmallIntegerField(default=1, unique=True)
    mom_weight = models.TextField()
    weight = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    food = models.TextField()
    title = models.TextField()
    content = models.TextField()
    advices = models.TextField()
    fruit_img = models.ImageField(upload_to="images/", blank=True, null=True)
    baby_img = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title


class Essentials(models.Model):
    title = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=256)
    answer = models.TextField()

    def __str__(self):
        return f'{self.question}'
