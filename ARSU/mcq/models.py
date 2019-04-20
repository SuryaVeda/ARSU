from django.db import models
from notes.models import subject
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Topic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=False)
    heading = models.CharField(max_length = 20, blank = False)
    def __str__(self):
        return self.heading

class Mcq(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=False)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=False)
    question = models.CharField(max_length = 70, blank = False)
    answer = models.CharField(max_length = 40, blank = False)
    image = models.ImageField(blank=True, null = True, upload_to = 'mcqs/images/%Y/%m/$D/')
    def __str__(self):
        return self.question
