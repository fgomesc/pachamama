from django.db import models
from django.urls import reverse


class Permissao(models.Model):
    tipo_permissao = models.CharField(max_length=70)



    def get_absolute_url(self):
        return reverse('list_permissao')


    def __str__(self):
        return self.tipo_permissao