from django.db import models
from django.contrib.auth.models import User
import uuid

class permiso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.TextField(blank=True, null=True)
    ult_actualizacion = models.DateTimeField(auto_now_add=True)
    ult_vez = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)

class Detallepermiso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    permiso = models.ForeignKey(permiso, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    ult_actualizacion = models.DateTimeField(auto_now_add=True)
    ult_vez = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)

class roles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Detallepermiso = models.ForeignKey(Detallepermiso, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    ult_actualizacion = models.DateTimeField(auto_now_add=True)
    ult_vez = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)
    
class Detalleroles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    roles = models.ForeignKey(roles, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    ult_actualizacion = models.DateTimeField(auto_now_add=True)
    ult_vez = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)