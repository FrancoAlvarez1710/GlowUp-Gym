from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    nombre = models.CharField(max_length=50) 
    descripcion = models.TextField(blank=True, null=True) 
    TIPO_ACTIVIDAD = [
        ('musculacion', 'Musculación'),
        ('yoga', 'Yoga'),
        ('crossfit', 'Crossfit'),
        ('funcional', 'Entrenamiento Funcional'),
        ('pilates', 'Pilates'),
        ('otro', 'Otro'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_ACTIVIDAD, default='otro')  
    duracion = models.IntegerField()  
    instructor = models.CharField(max_length=50)  
    costo = models.DecimalField(max_digits=8, decimal_places=2) 
    dias_disponibles = models.CharField(max_length=100)  
    horario = models.TimeField()

    def __str__(self):
        return f"Nombre: {self.nombre}"
    
class Rutina(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField() 
    duracion_minutos = models.PositiveIntegerField()  
    profesor = models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)  
    apellido = models.CharField(max_length=50)  
    email = models.EmailField()  
    telefono = models.CharField(max_length=15, null=True, blank=True) 
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)  
    apellido = models.CharField(max_length=50)  
    email = models.EmailField() 
    telefono = models.CharField(max_length=15, null=True, blank=True)  
    PLAN_VIGENTE_CHOICES = [
        ('musculacion', 'Musculación'),
        ('yoga', 'Yoga'),
        ('crossfit', 'Crossfit'),
        ('funcional', 'Entrenamiento Funcional'),
        ('pilates', 'Pilates'),
        ('otro', 'Otro'),
        ]
    plan = models.CharField(max_length=20, choices=PLAN_VIGENTE_CHOICES, default='otro')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    foto=models.ImageField(upload_to="profile_picture/", null=True,blank=True)