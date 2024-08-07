from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# TEMPLATE PARA CREAR FORMULARIO

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','precioNormal','precioSub','stock','tipo','imagen']
    
        widgets = {
                'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        }

class UsuarioForm(ModelForm):
        
    contrasena = forms.CharField(widget=forms.PasswordInput,min_length=8)
        
    class Meta:
        model = Usuario
        fields = ['run','nombre','apellido','correo','contrasena']
        
        widgets = {
                'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        }
#en uso este formulario de usuario 
class FormularioUserResgistro(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1','password2']

class SuscriptorForm(ModelForm):

    class Meta:
        model = Suscriptor
        fields = ['email','sub']

     