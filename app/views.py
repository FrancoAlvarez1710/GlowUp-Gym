from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profesor, Plan, Alumno
from .forms import PlanesFormulario, ProfesorFormulario, AlumnoFormulario

def Inicio(request):
    return render(request,"app/index.html")

def Planes(request):
    query = request.GET.get('q')
    if query:
        planes = Plan.objects.filter(nombre__icontains=query)
    else:
        planes=Plan.objects.all()
    return render(request,"app/index2.html", {"planes":planes})  

def Profesores(request):
    query = request.GET.get('q')
    if query:
        profes = Profesor.objects.filter(nombre__icontains=query)
    else:
        profes=Profesor.objects.all()
    return render(request,"app/profesores.html", {"profes":profes})

def Alumnos(request):
    query = request.GET.get('q')
    if query:
        alumnos = Alumno.objects.filter(nombre__icontains=query)
    else:
        alumnos=Alumno.objects.all()
    return render(request,"app/alumnos.html", {"alumnos":alumnos})

def Mi_rutina(request):
    return render(request,"app/mi-plan.html")

def formulario_planes(request):
    if request.method == "POST":
        form_planes = PlanesFormulario(request.POST)  
        if form_planes.is_valid():
            informacion_limpia = form_planes.cleaned_data 
            Plan.objects.create(
                nombre=informacion_limpia["nombre"], 
                descripcion=informacion_limpia["descripcion"], 
                tipo=informacion_limpia["tipo"], 
                duracion=informacion_limpia["duracion"], 
                instructor=informacion_limpia["instructor"], 
                costo=informacion_limpia["costo"], 
                dias_disponibles=informacion_limpia["dias_disponibles"], 
                horario=informacion_limpia["horario"]
            )
            return redirect("planes") 
    else:
        form_planes = PlanesFormulario()
    return render(request, "app/forms/formulario_planes.html", {"forms": form_planes})


def formulario_profesor(request):
    if request.method == "POST":
        form_profesor = ProfesorFormulario(request.POST)
        if form_profesor.is_valid():
           informacion_limpia=form_profesor.cleaned_data
           Profesor.objects.create(
            nombre=informacion_limpia["nombre"],  
            apellido=informacion_limpia["apellido"],
            email=informacion_limpia["email"],
            telefono=informacion_limpia["telefono"],
           )
           return redirect('profesores') 
    else:
        form_profesor = ProfesorFormulario()

    return render(request, 'app/forms/formulario_profesores.html', {'forms': form_profesor})

def formulario_alumno(request):
    if request.method == "POST":
        form_alumno = AlumnoFormulario(request.POST)
        if form_alumno.is_valid():
            informacion_limpia = form_alumno.cleaned_data
            Alumno.objects.create(
                nombre=informacion_limpia["nombre"],
                apellido=informacion_limpia["apellido"],
                email=informacion_limpia["email"],
                telefono=informacion_limpia["telefono"],
                plan=informacion_limpia["plan"],
            )
            return redirect('alumnos') 
    else:
        form_alumno = AlumnoFormulario()

    return render(request, 'app/forms/formulario_alumnos.html', {'forms': form_alumno})
