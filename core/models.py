from django.db import models


class Client(models.Model):
    """A company that uses the SaaS"""

    STATUS_CHOICES = (
        ("active", "Active"),
        ("pending", "Pending"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    )
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.status}"
