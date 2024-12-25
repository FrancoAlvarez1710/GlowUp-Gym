from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profesor, Plan, Alumno, Perfil
from .forms import PlanesFormulario, ProfesorFormulario, AlumnoFormulario, Editar_usuario, Perfilforms
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm 
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

def Inicio(request):
    return render(request,"app/index.html")

def Planes(request):
    query = request.GET.get('q')
    if query:
        planes = Plan.objects.filter(nombre__icontains=query)
    else:
        planes=Plan.objects.all()
    return render(request,"app/index2.html", {"planes":planes})  

@login_required(login_url="login")
def Profesores(request):
    query = request.GET.get('q')
    if query:
        profes = Profesor.objects.filter(nombre__icontains=query)
    else:
        profes=Profesor.objects.all()
    return render(request,"app/profesores.html", {"profes":profes})

@login_required(login_url="login")
def Alumnos(request):
    query = request.GET.get('q')
    if query:
        alumnos = Alumno.objects.filter(nombre__icontains=query)
    else:
        alumnos=Alumno.objects.all()
    return render(request,"app/alumnos.html", {"alumnos":alumnos})

def Mi_rutina(request):
    return render(request,"app/mi-plan.html")

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
def eliminar_alumno(request, id):
    alumno=Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('alumnos')

@login_required(login_url="login")
def eliminar_plan(request, id):
    plan=Plan.objects.get(id=id)
    plan.delete()
    return redirect('planes')

@login_required(login_url="login")
def eliminar_profesor(request, id):
    profe=Profesor.objects.get(id=id)
    profe.delete()
    return redirect('profesores')

@login_required(login_url="login")
def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        form_alumno = AlumnoFormulario(request.POST)
        if form_alumno.is_valid():
            informacion_limpia = form_alumno.cleaned_data
            print(informacion_limpia) 
            alumno.nombre = informacion_limpia["nombre"]
            alumno.apellido = informacion_limpia["apellido"]
            alumno.email = informacion_limpia["email"]
            alumno.telefono = informacion_limpia["telefono"]
            alumno.plan = informacion_limpia["plan"]
            alumno.save()
            return redirect("alumnos")
        else:
            print(form_alumno.errors) 
    else:
        form_alumno = AlumnoFormulario(initial={
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "email": alumno.email,
            "telefono": alumno.telefono,
            "plan": alumno.plan
        })

    return render(request, "app/forms/editar_alumnos.html", {"forms": form_alumno})

@login_required(login_url="login")
def editar_profesor(request, id):
    profe=Profesor.objects.get(id=id)
    if request.method=="POST":
        form_profesor = ProfesorFormulario(request.POST)
        if form_profesor.is_valid():
            informacion_limpia = form_profesor.cleaned_data
            print(informacion_limpia)
            profe.nombre=informacion_limpia["nombre"]
            profe.apellido=informacion_limpia["apellido"]
            profe.email=informacion_limpia["email"]
            profe.telefono=informacion_limpia["telefono"]
            profe.save()
        else:
            print(form_profesor.errors)
        return redirect("profesores")
    else:
        form_profesor = ProfesorFormulario(initial={"nombre":profe.nombre, "apellido":profe.apellido, "email": profe.email, "telefono":profe.telefono})
    return render(request, "app/forms/editar_profesor.html", {"forms":form_profesor})

@login_required(login_url="login")
def editar_plan(request, id):
    planes=Plan.objects.get(id=id)
    if request.method=="POST":
        form_planes = PlanesFormulario(request.POST)  
        if form_planes.is_valid():
            informacion_limpia = form_planes.cleaned_data
            planes.nombre=informacion_limpia["nombre"]
            planes.descripcion=informacion_limpia["descripcion"]
            planes.tipo=informacion_limpia["tipo"]
            planes.duracion=informacion_limpia["duracion"]
            planes.instructor=informacion_limpia["instructor"]
            planes.costo=informacion_limpia["costo"]
            planes.dias_disponibles=informacion_limpia["dias_disponibles"]
            planes.horario=informacion_limpia["horario"]
            planes.save()
        return redirect("planes")
    else:
        form_planes = PlanesFormulario(initial=
        {"nombre":planes.nombre, 
         "descripcion":planes.descripcion, 
         "tipo": planes.tipo, 
         "duracion":planes.duracion,
         "instructor":planes.instructor,
         "costo":planes.costo,
         "dias_disponibles":planes.dias_disponibles,
         "horario":planes.horario})
    return render(request, "app/forms/editar_plan.html", {"forms":form_planes})

def inicio_de_sesion(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        usuario=authenticate(request, username=username, password=password)
        if usuario is not None: 
            login(request,usuario)
            return redirect("inicio")
        else:
            return render(request, "app/forms/login.html")
    else:
        return render(request, "app/forms/login.html")

def desconexion_de_sesion(request):
    logout(request)
    return render(request, "app/index.html")

def registro(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form=UserCreationForm() 
    return render(request, "app/forms/registro.html", {"form":form})

def mostrar_perfil(request):
    return render(request, "app/mostrar-petfil.html")

def editar_perfil(request):

    usuario=request.user
    perfil, _ = Perfil.objects.get_or_create(usuario=usuario)

    if request.method=="POST":
        user_form=Editar_usuario(request.POST,instance=usuario)
        profile_form = Perfilforms(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect("mostrar-perfil")
        else: 
            return redirect("editar-perfil")
    else:   
        user_form=Editar_usuario(instance=usuario)
        profile_form=Perfilforms(instance=perfil)
    return render(request, "app/forms/editar-petfil.html", {"user_form":user_form, "profile_form":profile_form})
   
def cambiar_contraseña(request):
    usuario=request.user
    if request.method=="POST":
        form_password=PasswordChangeForm(usuario,request.POST)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, usuario)
            return redirect("inicio")
        else:
            return redirect("cambiar-contraseña")
    else:
        form_password=PasswordChangeForm(usuario)
    return render(request, "app/forms/cambiar-contraseña.html",{"form_passwprd":form_password})

def acerca(request):
    return render(request,"app/acerca.html")