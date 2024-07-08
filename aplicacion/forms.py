from django import forms
from .models import Persona, Producto
from .enumeraciones import *
from django.contrib.auth.forms import UserCreationForm

class CrearCuentaForm(UserCreationForm):
    pass

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, error_messages={"required": "Ingrese el nombre producto"})
    tipo_producto = forms.ChoiceField(choices=TIPO_PRODUCTO, error_messages={"required": "Seleccione tipo de producto"})
    precio = forms.IntegerField(min_value=1000, error_messages={"required": "Ingrese precio de producto"})
    stock = forms.IntegerField(min_value=0)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Producto
        fields = ['nombre', 'tipo_producto','precio', 'stock', 'imagen']

class UpdateProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, error_messages= {"required":"Ingrese su nombre"}, 
                        help_text="Debe ingresar su nombre")
    tipo_producto = forms.CharField(max_length=50, error_messages= {"required":"Ingrese el tipo de producto"}, 
                        help_text="Debe ingresar que tipo de producto es")
    
    precio = forms.IntegerField(min_value= 0 , error_messages= {"required":"Ingrese el precio"}, 
                        help_text="Debe ingresar el valor del producto")
    class Meta:
        model = Producto
        fields = ['nombre','tipo_producto', 'precio', 'stock', 'imagen']
    
class PersonaForm(forms.ModelForm):
    cod_persona=forms.CharField(max_length=10,
                        error_messages={"required":"Ingrese el primer nombre"}, 
                        help_text="Debe ingresar el nombre")
    

    class Meta:
        model = Persona
        fields = ['cod_persona','pnombre','snombre',
                  'apellidop','apellidom', 'correo',
                  'direccion', 'celular', 'region', 
                  'info_adicional', 'imagen']

class UpdatePersonaForm(forms.ModelForm):
    
    cod_persona=forms.CharField(max_length=10,
                        error_messages={"required":"Ingrese el primer nombre"}, 
                        help_text="Debe ingresar el nombre")
    

    class Meta:
        model = Persona
        fields = ['cod_persona','pnombre','snombre',
                  'apellidop','apellidom', 'correo',
                  'direccion', 'celular', 'region', 
                  'info_adicional', 'imagen']
        
class UsuarioForm(forms.ModelForm):
    nombusuario =forms.CharField(max_length=18,
                        error_messages={"required":"Ingrese nombre de usuario"}, 
                        help_text="Debe ingresar usuario")
    pwd =forms.CharField(max_length=18,
                        error_messages={"required":"Ingrese su contraseña"}, 
                        help_text="Contraseña no valida o vacia")
    class Meta:
        model = Persona
        fields = ['nombusuario', 'pwd']

class UpdateUsuarioForm(forms.ModelForm):
    nombusuario =forms.CharField(max_length=18,
                        error_messages={"required":"Ingrese nombre de usuario"}, 
                        help_text="Debe ingresar usuario")
    pwd =forms.CharField(max_length=18,
                        error_messages={"required":"Ingrese su contraseña"}, 
                        help_text="Contraseña no valida o vacia")
    class Meta:
        model = Persona
        fields = ['nombusuario', 'pwd']

class EnvioForm(forms.ModelForm):
    fecha_compra = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    usuario      = forms.CharField(max_length=18, error_messages={"required":"Ingrese nombre de usuario"}, 
                                   help_text="Debe ingresar usuario")
    
class Meta:
     model = Persona
     fields = ['fecha_compra', 'usuario']
     
class UpdateEnvioForm(forms.ModelForm):
    fecha_compra = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    usuario      = forms.CharField(max_length=18, error_messages={"required":"Ingrese nombre de usuario"}, 
                                   help_text="Debe ingresar usuario")
    
class Meta:
     model = Persona
     fields = ['fecha_compra', 'usuario']
     

class CarritoForm(forms.ModelForm):
    usuario      = forms.CharField(max_length=18, error_messages={"required":"Ingrese nombre de usuario"}, 
                                   help_text="Debe ingresar usuario")
    
class Meta:
     model = Persona
     fields = ['usuario', 'envio', 'producto', 'cantidad']
     
class UpdateCarritoForm(forms.ModelForm):
    usuario      = forms.CharField(max_length=18, error_messages={"required":"Ingrese nombre de usuario"}, 
                                   help_text="Debe ingresar usuario")
    
class Meta:
     model = Persona
     fields = ['usuario', 'envio', 'producto', 'cantidad']
     
     
     
     
