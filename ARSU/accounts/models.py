from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from batches.models import batches


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
        user.active = True
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
    active = models.BooleanField(default = True)
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
    def is_active(self):
        return self.active
