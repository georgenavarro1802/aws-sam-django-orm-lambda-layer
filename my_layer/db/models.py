import uuid

from django.db import models

from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from db.helpers import *


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(blank=True, null=True, db_index=True)
    updated_at = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        abstract = True

    def get_id(self):
        return self.id.__str__()


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=USER_ROLES, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.get_full_name()} ({self.email})'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
        managed = False

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
        return full_name.strip()

    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission? Simplest possible answer: Yes, always
        """
        return True

    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?"
        Simplest possible answer: Yes, always
        """
        return True
