from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Clubs(models.Model):
    heading = models.CharField(max_length = 30)
    image = models.ImageField(default = True, null = True, upload_to = 'clubs/images/%Y/%m/$D/')
    text = models.CharField(max_length = 30, blank = True)
    def __str__(self):
        return self.heading
class details(models.Model):
    post = models.ForeignKey(Clubs, on_delete=models.SET_NULL, null=True, blank=True)
    heading =models.CharField(max_length = 30, blank = True)
    img = models.ImageField(upload_to = 'clubs/images/%Y/%m/$D/', blank = True, default = None)
    def __str__(self):
        return self.heading
class Events(models.Model):
    post = models.ForeignKey(details, on_delete=models.SET_NULL, null=True, blank=True)
    month = models.CharField(max_length = 6)
    date = models.CharField(max_length = 6)
    heading = models.CharField(max_length = 30)
    text = models .CharField(max_length = 80, blank = True)
    image = models.ImageField(blank=True, null = True, upload_to = 'clubs/images/%Y/%m/$D/')
    def __str__(self):
        return self.heading
