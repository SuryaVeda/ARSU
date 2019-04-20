from django.db import models

# Create your models here.
class Student(models.Model):
    heading = models.CharField(max_length = 20, blank = False)
    name = models.CharField(max_length=40, blank = False)
    batch = models.CharField(max_length = 20, blank = False)
    phone = models.IntegerField(blank = False)
    email = models.EmailField(max_length= 30, blank = False)
    image = models.ImageField(blank=True, null = True, upload_to = 'body/images/%Y/%m/$D/')
    def __str__(self):
        return self.heading

class Detail(models.Model):
    heading = models.CharField(max_length = 20, blank = False)
    text = models.CharField(max_length= 1000, blank = False)
    def __str__(self):
        return self.heading
