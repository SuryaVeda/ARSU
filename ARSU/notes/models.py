from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
# Create your models here.
class EbookManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(heading__icontains=query))
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    heading = models.CharField(max_length = 20, blank = False)
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    objects = EbookManager()
    def __str__(self):
        return self.heading
class Ebook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=True)
    pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    link = models.URLField(blank=True, null = True,max_length = 1500)
    heading = models.CharField(max_length=30)
    objects = EbookManager()
    def __str__(self):
        return self.heading
class Lecture(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=True)
    pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    heading = models.CharField(max_length=30)
    link = models.URLField(blank=True, null = True,max_length = 1500)
    objects = EbookManager()
    def __str__(self):
        return self.heading
class Paper(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True, blank=True)
    pdf = models.FileField(blank=True, null = True, upload_to = "pdf/%Y/%m/$D/")
    image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
    heading = models.CharField(max_length=30)
    link = models.URLField(blank=True, null = True,max_length = 1500)
    objects = EbookManager()
    def __str__(self):
        return self.heading
