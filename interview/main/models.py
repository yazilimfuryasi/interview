from django.db import models

class digitalArt(models.Model):
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    mouth = models.CharField(max_length=200)
    clothes = models.CharField(max_length=200)
    bg = models.CharField(max_length=200)
    eyes = models.CharField(max_length=200)
    fur = models.CharField(max_length=200)