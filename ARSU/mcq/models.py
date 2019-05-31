from django.db import models
from notes.models import subject
from django.contrib.auth.models import User
from django.conf import settings

class Topic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=False)
    heading = models.CharField(max_length = 20, blank = False)
    def __str__(self):
        return self.heading

class Mcq(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=False)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=False)
    question = models.CharField(max_length = 1270, blank = False)
    option_one =  models.CharField(max_length = 270, blank = True, null = True)
    option_two =  models.CharField(max_length = 270, blank = True, null = True)
    option_three =  models.CharField(max_length = 270, blank = True, null = True)
    option_four =  models.CharField(max_length = 270, blank = True, null = True)
    answer = models.CharField(max_length = 140, blank = False)
    q_image = models.ImageField(blank=True, null = True, upload_to = 'mcqs/images/%Y/%m/$D/')
    a_image = models.ImageField(blank=True, null = True, upload_to = 'mcqs/images/%Y/%m/$D/')
    def __str__(self):
        return self.question
class FlashCard(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=False)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=False)
    question = models.CharField(max_length = 5270, blank = False)
    answer = models.CharField(max_length = 2540, blank = False)
    q_image = models.ImageField(blank=True, null = True, upload_to = 'mcqs/images/%Y/%m/$D/')
    a_image = models.ImageField(blank=True, null = True, upload_to = 'mcqs/images/%Y/%m/$D/')
    def __str__(self):
        return self.question
class Fact(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=False)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=False)
    answer = models.CharField(max_length = 540, blank = False)
    image = models.ImageField(blank=True, null = True, upload_to = 'mcqs/images/%Y/%m/$D/')
    def __str__(self):
        return self.answer
