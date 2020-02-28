from django.db import models
from django.urls import reverse


class Perfil(models.Model):
    tipo_perfil = models.CharField(max_length=70)

    def get_absolute_url(self):
        return reverse('list_perfil')


    def __str__(self):
        return self.tipo_perfil