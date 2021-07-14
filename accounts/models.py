from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    info = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f"Profile of user {self.user}"
