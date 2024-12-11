from django import forms

class PlanesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)  
    descripcion = forms.CharField(widget=forms.Textarea, required=False)  
    TIPO_ACTIVIDAD = [
        ('musculacion', 'Musculación'),
        ('yoga', 'Yoga'),
        ('crossfit', 'Crossfit'),
        ('funcional', 'Entrenamiento Funcional'),
        ('pilates', 'Pilates'),
        ('otro', 'Otro'),
    ]
    tipo = forms.ChoiceField(choices=TIPO_ACTIVIDAD, initial='otro')  
    duracion = forms.IntegerField() 
    instructor = forms.CharField(max_length=50)  
    costo = forms.DecimalField(max_digits=8, decimal_places=2) 
    dias_disponibles = forms.CharField(max_length=100)  
    horario = forms.TimeField()  

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50) 
    apellido = forms.CharField(max_length=50)  
    email = forms.EmailField()  
    telefono = forms.CharField(max_length=15, required=False) 

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}))
    telefono = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono (opcional)'}))
    PLAN_VIGENTE_CHOICES = [
        ('musculacion', 'Musculación'),
        ('yoga', 'Yoga'),
        ('crossfit', 'Crossfit'),
        ('funcional', 'Entrenamiento Funcional'),
        ('pilates', 'Pilates'),
        ('otro', 'Otro'),
    ]
    plan = forms.ChoiceField(choices=PLAN_VIGENTE_CHOICES, initial='otro', widget=forms.Select(attrs={'class': 'form-control'}))