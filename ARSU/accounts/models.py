from django.db import models
import datetime
from datetime import date, timedelta
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from home.models import batches

class UserManager(BaseUserManager):
    def create_user(self, email,username, password = None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_visitor(self, email, username, password):
        user = self.create_user(
            email = email,
            password=password,
            username = username,
        )
        user.outsider = True

        user.save(using=self._db)
        return user
    def create_student(self, email, username,password):
        user = self.create_user(
            email = email,
            password=password,
            username = username,
        )
        user.student = True

        user.save(using=self._db)
        return user
    def create_cr(self, email, username,password):
        user = self.create_user(
            email = email,
            password=password,
            username = username,
        )
        user.cr = True
        user.student = True

        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = email,
            password=password,
            username = username,
        )
        user.admin = True
        user.student = True
        user.staff = True
        user.is_active = True
        user.cr = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    batch = models.ForeignKey(batches,on_delete = models.CASCADE,  null = True, blank = True)
    email = models.EmailField(max_length =255, unique = True)
    username = models.CharField(max_length = 20)
    outsider = models.BooleanField(default = False)
    student = models.BooleanField(default = False)
    cr = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_outsider(self):
        return self.outsider
    @property
    def is_student(self):
        return self.student
    @property
    def is_cr(self):
        return self.cr
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def get_email(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    backgroundImage = models.ImageField(blank=True, null = True, upload_to = 'profiles/images/%Y/%m/$D/')
    profilePic = models.ImageField(blank=True, null = True, upload_to = 'profiles/images/%Y/%m/$D/')
    name = models.CharField(max_length =50, blank=True, null = True)
    dob = models.DateField(blank=True, null = True)
    batch = models.ForeignKey(batches,on_delete = models.CASCADE,  null = True, blank = True)
    hobbies = models.CharField(max_length =50,blank=True, null = True)
    about = models.CharField(max_length =500,blank=True, null = True)
    quotes = models.CharField(max_length =300,blank=True, null = True)
    links = models.URLField(max_length =500,blank=True, null = True)
    phone = models.IntegerField(blank=True, null = True)
    email = models.EmailField(blank = False, null = False)
    def __str__(self):

        return self.name


class Timetable(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    fromDate = models.DateField(blank = False, null = False)
    toDate = models.DateField(blank = False, null = False)
    heading = models.CharField(max_length =50,blank=True, null = True)
    def date_range(self):
        return list(map(date.fromordinal, range(self.fromDate.toordinal(), self.toDate.toordinal()+1)))
    def __str__(self):
        return self.heading

class Activites(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    table = models.ForeignKey(Timetable,on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(blank = False, null = True)
    heading = models.CharField(max_length =50)
    text = models.CharField(max_length =50, null=True, blank=True)
    def __str__(self):
        return self.heading
class Remainders(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length =80)
    def delete(self):
        return Remainders.objects.filter(text = self.text).delete()
