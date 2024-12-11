from django.urls import path
from app.views import Inicio, Planes, Profesores, Alumnos, Mi_rutina, formulario_planes, formulario_profesor, formulario_alumno
urlpatterns = [
    path('inicio/', Inicio, name='inicio'),
    path('planes/', Planes, name='planes'), 
    path('profesores/', Profesores, name='profesores'),
    path('alumnos/', Alumnos, name='alumnos'), 
    path('mirutina/', Mi_rutina, name='mirutina'), 
    path('formularioplanes/', formulario_planes, name='formularioplanes'), 
    path('formularioprofesores/', formulario_profesor, name='formularioprofesores'),
    path('formularioalumnos/', formulario_alumno, name='formularioalumnos'),


]