from django.db import models

from appli.models.image import Image


class Dossier(models.Model):

    nom = models.CharField(max_length=100, default='')
    images = models.ManyToManyField(Image)