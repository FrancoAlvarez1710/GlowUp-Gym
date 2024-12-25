from django.urls import path
from app.views import Inicio, Planes, Profesores, Alumnos, Mi_rutina, formulario_planes, formulario_profesor, formulario_alumno, eliminar_profesor, eliminar_alumno, eliminar_plan, editar_alumno, editar_profesor, editar_plan, inicio_de_sesion, desconexion_de_sesion, registro, mostrar_perfil, editar_perfil, cambiar_contraseña, acerca
urlpatterns = [
    path('inicio/', Inicio, name='inicio'),
    path('planes/', Planes, name='planes'), 
    path('profesores/', Profesores, name='profesores'),
    path('alumnos/', Alumnos, name='alumnos'), 
    path('mirutina/', Mi_rutina, name='mirutina'), 
    path('formularioplanes/', formulario_planes, name='formularioplanes'), 
    path('formularioprofesores/', formulario_profesor, name='formularioprofesores'),
    path('formularioalumnos/', formulario_alumno, name='formularioalumnos'),
    path('eliminaralumnos/<int:id>', eliminar_alumno, name='eliminaralumnos'),
    path('eliminarplan/<int:id>', eliminar_plan, name='eliminarplan'),
    path('eliminarprofesor/<int:id>', eliminar_profesor, name='eliminarprofesor'),
    path('editaralumnos/<int:id>', editar_alumno, name='editaralumnos'),
    path('editarprofesor/<int:id>', editar_profesor, name='editarprofesor'),
    path('editarplan/<int:id>', editar_plan, name='editarplan'),
    path('login/', inicio_de_sesion, name='login'),
    path('logout/', desconexion_de_sesion, name='logout'),
    path('registro/', registro, name='registro'),
    path('mostrar-perfil/', mostrar_perfil, name='mostrar-perfil'),
    path('editar-perfil/', editar_perfil, name='editar-perfil'),
    path('cambiar-contraseña/', cambiar_contraseña, name='cambiar-contraseña'),
    path('acerca/', acerca, name='acerca'),
    

]