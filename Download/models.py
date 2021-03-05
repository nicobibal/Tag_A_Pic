from django.db import models

class Profil(models.Model):
    username = models.CharField(max_length=50)