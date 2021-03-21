from django.db import models
from django.contrib.auth.models import AbstractUser


USER_GENDER = (("Male", "Male"), ("Female", "Female"),
               ("Prefer not to say", "Prefer not to say"))

class User(AbstractUser):
    username = models.CharField(
        max_length=100, null=True, blank=True, unique=True)
    email = models.CharField(max_length=100, null=True,
                             blank=True, unique=True)
    remember_token = models.CharField(max_length=255, null=True)
    token_expiry = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=20, null=True,
                              blank=True, choices=USER_GENDER)
    email_verifY_token = models.CharField(
        max_length=255, null=True, blank=True)
    email_verifY_token_expiry = models.DateTimeField(blank=True, null=True)
    email_verifY = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=1)

    class Meta:
        managed = True
        db_table = 'tbl_user'

class Services(models.Model):
    name=models.CharField(max_length=255, null=True)
    description=models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)

class listService(models.Model):
    name=models.CharField(max_length=255, null=True)
    service = models.ManyToManyField(Services,related_name="list_services")


