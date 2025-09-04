from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Client


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

    def __str__(self):
        return f"{self.email} ({self.role})"
