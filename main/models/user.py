from django.db import models    
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, uuid, password=None, **extra_fields):
        user = self.model(uuid=uuid, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, uuid, password=None):
        return self.create_user(uuid)

class User(AbstractBaseUser):
    uuid = models.CharField(primary_key=True, max_length=128, unique=True)
    USERNAME_FIELD = 'uuid'
    objects = UserManager()