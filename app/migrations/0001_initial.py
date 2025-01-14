# Generated by Django 5.1.3 on 2024-12-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mi_rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaDeEntrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('musculacion', 'Musculación'), ('yoga', 'Yoga'), ('crossfit', 'Crossfit'), ('funcional', 'Entrenamiento Funcional'), ('pilates', 'Pilates'), ('otro', 'Otro')], default='otro', max_length=20)),
                ('duracion', models.IntegerField()),
                ('instructor', models.CharField(max_length=50)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dias_disponibles', models.CharField(max_length=100)),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
