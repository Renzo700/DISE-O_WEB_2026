from django.db import models
from django.contrib.auth.models import User
import uuid

class Personas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"