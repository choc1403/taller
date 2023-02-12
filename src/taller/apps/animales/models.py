from django.db import models

# Create your models here.
class Animal(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre