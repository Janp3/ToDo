from django.db import models

# Create your models here.


class task(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=255)
    date = models.DateField(
        auto_now=False, auto_now_add=False)
