# Create your views here.

from django.shortcuts import redirect, render

from . import forms, models

def index(request):
    return render(request, "aplicacion/index.html")


def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "aplicacion/profesor_list.html", contexto)


def profesor_create(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor_list")
    else:
        form = forms.ProfesorForm()
    return render(request, "aplicacion/profesor_create.html", {"form": form})

def estudiante_list(request):
    consulta = models.Estudiante.objects.all()
    contexto = {"estudiantes": consulta}
    return render(request, "aplicacion/estudiante_list.html", contexto)


def estudiante_create(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = forms.EstudianteForm()
    return render(request, "aplicacion/estudiante_create.html", {"form": form})

def curso_list(request):
    consulta = models.Curso.objects.all()
    contexto = {"cursos": consulta}
    return render(request, "aplicacion/curso_list.html", contexto)


def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:
        form = forms.CursoForm()
    return render(request, "aplicacion/curso_create.html", {"form": form})

