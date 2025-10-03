from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """custom user manager to handle user creation"""
    def create_user(self, email, password=none, **extra_fields):
        if not email:
            raise ValueError("email address is compulsory for all users.")
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return superuser"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_super_user = True

        user.save(using= self._db)

        return user    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=true)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
    