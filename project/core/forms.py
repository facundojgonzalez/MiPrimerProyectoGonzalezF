from django import forms

from . import models


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = models.Alumno
        fields = "__all__"
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"

