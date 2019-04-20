from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    heading = models.CharField(max_length = 20, blank = False)
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    def __str__(self):
        return self.heading
class sideHeading(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=True)
    ebooks_pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    lectures_pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    papers_pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    heading = models.CharField(max_length=30)
    def __str__(self):
        return self.heading
