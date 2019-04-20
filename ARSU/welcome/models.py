from django.db import models

# Create your models here.
class slider(models.Model):
    image = models.ImageField(blank=True, null = True, upload_to = 'carousel/%Y/%m/$D/')
