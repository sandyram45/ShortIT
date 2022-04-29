from django.db import models

# Create your models here.


class urlEntry(models.Model):
    url = models.URLField()
    shortened_url = models.URLField(max_length=30)

    def __str__(self):
        return self.url



