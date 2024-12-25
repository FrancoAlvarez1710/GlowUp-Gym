# GlowUp Gym
## Descripción
GlowUp Gym es un sitio web de un gimnasio ficticio,  donde se pueden gestionar planes de entrenamiento, alumnos y profesores. Este proyecto está diseñado en Django y tiene una interfaz de usuario construida con Bootstrap.

### Requisitos
- Python 3.x
- Django 5.x
- Bootstrap (para el diseño de la interfaz)
- Base de datos (SQLite por defecto)

>**Super usuario:**
>Usuario: franco     |     Contraseña: pi31415926
>
>**Usuario regular**:
>Usuario: Estanislao     |     Contraseña: pi31415926

### Instalación

1. **Clona el repositorio:**

` git clone https://github.com/FrancoAlvarez1710/GlowUp-Gym.git` 

###### Accede al proyecto:
 
` cd GlowUp-Gym` 

###### Aplicar migraciones de base de datos
 
` python manage.py migrate` 

###### Crear super usuario:
` python manage.py createsuperuser` 
acceder a las funcionalidades del administrador 
` http://127.0.0.1:8000/admin/` 

 ###### Correr el servidor:
 ` python manage.py runserver` 
 
*El servidor estará disponible en http://127.0.0.1:8000/.*   
 ##### Para ir al inicio de la página para oobservar todas las fucionalidades, debe dirigirse a la url de:

` http://127.0.0.1:8000/app/inicio` 
### Funcionalidades

#### 1. Planes:
Accede a la sección de Planes para ver todos los planes disponibles en el gimnasio.
Puedes agregar nuevos planes a través del botón de ` "Agregar plan` , el cual abrirá un formulario para completar con los datos del nuevo plan (nombre, tipo, costo).
Los planes deben mostrarse en una tabla donde cada fila representa un plan existente con sus detalles.

#### 2. Entrenadores:
En la sección de Entrenadores, podrás ver una lista de los entrenadores del gimnasio.
Similar a los planes, podrás agregar nuevos profesores usando un formulario que pide su nombre, especialidad, y contacto.
#### 3. Alumnos:
En la sección de Alumnos, podrás ver la lista de todos los alumnos registrados.
Cada alumno puede tener un plan de entrenamiento asignado.
Puedes agregar nuevos alumnos con sus detalles, incluyendo el nombre, apellido, correo, teléfono y el plan vigente que sigue (como "Musculación", "Yoga", etc.).

#### Formularios de inscripción:
Todos los campos cuentan con sus respectivos botones para agregar datos a los campos, al igual que formularios de búsqueda. 
