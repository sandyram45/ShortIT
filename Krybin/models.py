from django.db import models

# Create your models here.


class boxText(models.Model):
    text = models.TextField()
    copy_url = models.URLField()

    def __str__(self):
        return self.text
