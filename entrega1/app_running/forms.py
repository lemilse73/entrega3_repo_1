from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Corredor_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    modalidad = forms.CharField(max_length=10)
    email = forms.EmailField()
    team = forms.CharField(max_length=10)

class Carreras_formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    modalidad = forms.CharField(max_length=10)
    distancia= forms.IntegerField()
    fecha = forms.DateField()

class Teams_formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    modalidad = forms.CharField(max_length=10)
    email = forms.EmailField()


class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña" , widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['email' , 'password1' , 'password2' ]
        help_text = {k:"" for k in fields}

