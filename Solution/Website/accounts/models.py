from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, location, phone_number,  ccp, agr, img, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            location=location,
            ccp=ccp,
            desc='',
            img=img,
            agr=agr,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,  password):
        user = self.create_user(
            username=username,
            password=password,
            phone_number=0,
            location='',
            ccp=0,
            email=email,
            img='',
            agr='',

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin,):

    email = models.EmailField(verbose_name="email", max_length=80, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=400, null=True, blank=True)
    agr = models.FileField(max_length=255, upload_to='agr', null=True, blank=True)
    img = models.FileField(max_length=255, upload_to='images_association', null=True, blank=True)
    ccp = models.CharField(max_length=20, null=True, blank=True)
    desc = models.CharField(max_length=400, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = MyAccountManager()

    def __str__(self):
        return self.username
