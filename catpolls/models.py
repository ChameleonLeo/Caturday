import datetime

from django.db import models
from django.utils import timezone


class Catuestion(models.Model):
    catuestion_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    catuestion_image = models.ImageField(upload_to='polls-img/', default='polls-img/img23.jpg')

    def __str__(self):
        return self.catuestion_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now

    was_published_recently.admin_order_field = 'publication_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Cachoice(models.Model):
    catuestion = models.ForeignKey(Catuestion, on_delete=models.CASCADE)
    cachoice_text = models.CharField(max_length=200)
    cavotes = models.IntegerField(default=0)

    def __str__(self):
        return self.cachoice_text
