from django.db import models

# Create your models here.
class Tasks (models.Model):
    Persona_asignada=models.CharField(max_length=20)
    Titulo=models.CharField(max_length=40)
    Descripcion=models.TextField(blank=True)
    Estado=models.BooleanField(default=False)
    Archivo= models.FileField(upload_to='upload/')

    def __str__(self):
        return self.Titulo