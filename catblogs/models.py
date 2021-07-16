from django.db import models
from django.conf import settings
from django.utils import timezone


class CatPost(models.Model):
    catauthor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.SET_DEFAULT,
                                  default=19)
    catitle = models.CharField(max_length=200)
    catext = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.catitle
