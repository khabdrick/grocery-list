from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


CHOICES = (
    ("pending", "PENDING"),
    ("bought", "BOUGHT"),
    ("left", "LEFT"),
    ("not available", "NOT AVAILABLE"),
)


class Grocery(models.Model):

    user = models.ForeignKey(User, related_name="grocery", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, null=True, blank=True)
    item_quantity = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    item_status = models.CharField(
        max_length=255, null=True, blank=True, default="pending", choices=CHOICES
    )
    date = models.DateField(
        max_length=255,
        null=True,
        blank=True,
        auto_now_add=True
    )
    def __str__(self):
        return self.item_name
