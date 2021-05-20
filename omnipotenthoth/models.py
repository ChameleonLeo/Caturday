from django.db import models
# from django.core.files.storage import FileSystemStorage


class Tip(models.Model):
    tip_text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='thoth-img/')

    def __str__(self):
        return self.tip_text
