from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL


class Author(models.Model):
    """
    Author entity

    Provides first_name and last_name, since he/she can write under a Pen Name
    """
    user = models.ForeignKey(to=USER, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
