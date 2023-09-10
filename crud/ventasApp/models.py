from django.db import models
#from django.forms import ModelForm
from django.forms import ModelForm

# Create your models here.
class Producto(models.Model):
    producto_no=models.PositiveSmallIntegerField(primary_key=True)
    descripcion=models.CharField(max_length=30,blank=False)
    precio_actual=models.DecimalField(max_digits=8,decimal_places=2)
    stock_disponible=models.DecimalField(max_digits=8,decimal_places=0)

class Departamento(models.Model):
    depto_no=models.PositiveSmallIntegerField(primary_key=True)
    dnombre=models.CharField(max_length=14,blank=False)
    localidad=models.CharField(max_length=10,blank=False)


"""class departamentoForm(forms.Form):
    actualizar_localidad = forms.CharField(max_length=10,blank=False,help_text="Ingrese la nueva Localidad")"""

#creamos formulario para insertar
#formDepInsert=departamentoForm()

class Empleado(models.Model):
    emp_no=models.PositiveSmallIntegerField(primary_key=True)
    apellido=models.CharField(max_length=30,blank=False)
    oficio=models.CharField(max_length=10, blank=False)
    director=models.PositiveSmallIntegerField()
    fecha_alta=models.DateField()
    salario=models.DecimalField(max_digits=8,decimal_places=2)
    comision=models.DecimalField(max_digits=8,decimal_places=2)
    telefono=models.CharField(max_length=15)
    depto_no = models.ForeignKey(Departamento,default='1',blank=True,on_delete=models.CASCADE)

class Categoria(models.Model):
    categoria_no=models.PositiveSmallIntegerField(primary_key=True)
    descripcion=models.CharField(max_length=100,blank=False)

class detalleArticulo(models.Model):
    detalle_no=models.PositiveSmallIntegerField(primary_key=True)
    talla=models.PositiveSmallIntegerField()
    colores=models.CharField(max_length=15)
    imagen1=models.CharField(max_length=150)
    disponible=models.BooleanField()
    composicion=models.CharField(max_length=150)
    cuidados = models.CharField(max_length=150)
    envio=models.CharField(max_length=100)
    devolucion=models.CharField(max_length=100)
    
class Articulo(models.Model):
    articulo_no=models.PositiveSmallIntegerField(primary_key=True)
    imagen1=models.CharField(max_length=300)
    descripcion=models.CharField(max_length=300,blank=False)
    precio=models.DecimalField(max_digits=8,decimal_places=2)
    detalle_no=models.ForeignKey(detalleArticulo,default='0',blank=True,on_delete=models.CASCADE)
    

