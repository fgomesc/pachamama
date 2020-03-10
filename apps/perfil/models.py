from django.db import models
from django.urls import reverse


class Perfil(models.Model):
    STATUS_CHOICE=(('L', 'Lançador'), ('AP1', 'Aprovador Nível 1'), ('AP2', 'Aprovador Nível 2'))
    tipo_perfil = models.CharField(max_length=3, choices=STATUS_CHOICE, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('list_perfil')


    def __str__(self):
        return self.tipo_perfil