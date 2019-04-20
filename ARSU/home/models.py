from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class batches(models.Model):
    name = models.CharField(max_length = 40)
    css = models.CharField(max_length = 10, blank = True)
    jq = models.CharField(max_length = 10, blank = True)
    def __str__(self):
        return self.name
class Academic(models.Model):
    batches = models.ForeignKey(batches,on_delete=models.SET_NULL, null=True, blank=False)
    pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    heading = models.CharField(max_length = 40)
    text = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return self.heading


class NonAcademic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    heading = models.CharField(max_length = 40)
    text = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return self.heading

class HospitalNews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    heading = models.CharField(max_length = 40, blank = True)
    file = models.FileField(blank =True, null=True, upload_to = 'html/%Y/%m/$D/')
    summary = models.CharField(max_length = 300, blank = True)
    url = models.URLField(max_length=400, blank = True)

    def __str__(self):
        return self.heading

class CampusNews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    heading = models.CharField(max_length = 40, blank = True)
    file = models.FileField(blank =True, null=True, upload_to = 'html/%Y/%m/$D/')
    summary = models.CharField(max_length = 300, blank = True)

    def __str__(self):
        return self.heading
class Carousel(models.Model):
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
