from django.db import models

# Create your models here.


class DM(models.Model):
    city = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
