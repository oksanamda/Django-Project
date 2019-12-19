from django.db import models


# Create your models here.
class Phone(models.Model):
    number = models.CharField(max_length=12)
    code = models.CharField(max_length=6, default='000000')

    def __str__(self):
        return self.number
