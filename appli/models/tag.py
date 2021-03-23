from django.db import models


class Tag(models.Model):
    nom = models.CharField(max_length=50, default='');

