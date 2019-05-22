from django.db import models
from home.models import batches
# Create your models here.
class Student(models.Model):
    designation = models.CharField(max_length = 20, blank = False)
    name = models.CharField(max_length=40, blank = False)
    batch = models.ForeignKey(batches,on_delete = models.CASCADE,  null = True, blank = True)
    phone = models.IntegerField(blank = False)
    email = models.EmailField(max_length= 30, blank = False)
    image = models.ImageField(blank=True, null = True, upload_to = 'body/images/%Y/%m/$D/')
    def __str__(self):
        return self.designation

class Detail(models.Model):
    heading = models.CharField(max_length = 20, blank = False)
    text = models.CharField(max_length= 1000, blank = False)
    def __str__(self):
        return self.heading
