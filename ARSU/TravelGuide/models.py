from django.db import models
from accounts.models import User
# Create your models here.

class Travel(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    heading = models.CharField(max_length = 20, null = False, blank = False, default = "fuck")
    itinerary = models.CharField(max_length = 1000, null = True, blank = True)
    budget = models.CharField(max_length = 200, null = True, blank = True)
    experience = models.CharField(max_length = 150, null = True, blank = True)
    image = models.ImageField(upload_to='travel/images/%Y/%m/$D/', blank = False, default=None)
    def __str__(self):
        return self.heading

class Images(models.Model):
    post = models.ForeignKey(Travel, on_delete=models.SET_NULL, null=True,)
    image = models.ImageField(upload_to='travel/images/%Y/%m/$D/', null = True, blank = True)
    def __str__(self):
        return self.post.heading
