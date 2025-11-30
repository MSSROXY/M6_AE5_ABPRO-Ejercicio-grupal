from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    privado = models.BooleanField(default=False)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('eventos:listar_eventos')
