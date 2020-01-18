from django.db import models


class Resume(models.Model):
    file = models.FileField(upload_to="Resumes")


class Profile(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    template = models.CharField(max_length=200)
