from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Client


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """This is the model for Users.
    Used for Admin users (platform) and Client users (company)"""

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("client", "Client"),
        ("end_user", "End User"),
    )

    username = None
    email = models.EmailField(max_length=255, unique=True)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="client")
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,  # Deleting Client won't delete user
        null=True,
        blank=True,
        help_text="Only needed if role = client",
    )

    USERNAME_FIELD = "email"  # Using email as username
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"
