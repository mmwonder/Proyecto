from django.db import models 
from django.shortcuts import render,redirect
from ventasApp.models import Producto,Departamento,Empleado,Articulo,detalleArticulo
from django.views.generic import ListView,DetailView,UpdateView
from django.forms import ModelForm
from ventasApp.forms import departamentoForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

class ProductoListView(ListView):
    model=Producto
    template_name='productos.html'
    def get_queryset(self):
        return Producto.objects.all().filter(descripcion='TV',precio_actual__lt=30.00)

"""class DepartamentoModificarFormView(FormView):
    template_name = "modificarDepartamento.html"
    form_class = departamentoForm
    success_url = "/"
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)"""
    
class DepartamentoListView(ListView):
    model=Departamento
    template_name='departamentos.html'
    def get_queryset(self):
        return Departamento.objects.all()

"""class departamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields= ["depto_no","dnombre"]"""

class modificarDepartamento(UpdateView):
    model=Departamento
    fields=["localidad"]
    success_url = reverse_lazy("departamento-base")
    
    """#creamos departamento y formulario para modificar
    departamento=Departamento.objects.get(depto_no=uuid)
    formDepUpdate=departamentoForm(instance=departamento)
    template_name='departamentos.html' """


class EmpleadoListView(ListView):
    model=Empleado
    template_name='empleados.html'
    def get_queryset(self):
        queryset=self.model.objects.all()
        return queryset
class EmpleadoDetailView(DetailView):
    model=Departamento
    template_name='detalle.html'
    def get_object(self):
        objeto=self.model.objects.get(depto_no=self.kwargs['depto_no'])
        return objeto
    
def insertarProducto(request):
    var_producto_no=request.POST['producto_no']
    var_descripcion=request.POST['descripcion']
    var_precio_actual=request.POST['precio_actual']
    var_stock_disponible=request.POST['stock_disponible']

    producto=Producto.objects.create(producto_no=var_producto_no,
                                     descripcion=var_descripcion,
                                     precio_actual=var_precio_actual,
                                     stock_disponible=var_stock_disponible)
    return redirect('/verProducto')  

def insertarDepartamento(request):
    var_depto_no=request.POST['depto_no']
    var_dnombre=request.POST['dnombre']
    var_localidad=request.POST['localidad']

    departamento=Departamento.objects.create(depto_no=var_depto_no,
                                            dnombre=var_dnombre,
                                            localidad=var_localidad)
    return redirect('/verDepartamento') 

def insertarEmpleado(request):
    var_emp_no=request.POST['emp_no']
    var_apellido=request.POST['apellido']
    var_oficio=request.POST['oficio']
    var_director=request.POST['director']
    var_fecha_alta=request.POST['fecha_alta']
    var_salario=request.POST['salario']
    var_comision=request.POST['comision']
    var_telefono=request.POST['telefono']
    var_depto_no=request.POST['depto_no']

    Empleados=Empleado.objects.create(
        emp_no=var_emp_no,
        apellido=var_apellido,
        oficio=var_oficio,
        director=var_director,
        fecha_alta=var_fecha_alta,
        salario=var_salario,
        comision=var_comision,
        telefono=var_telefono,
        depto_no_id=var_depto_no

    )
    return redirect('/verEmpleado')

def eliminarProducto(request,prod_no):
    producto=Producto.objects.get(producto_no=prod_no)
    producto.delete()
    return redirect('/verProducto')

def eliminarDepartamento(request,dep_no):
    departamento=Departamento.objects.get(depto_no=dep_no)
    departamento.delete()
    return redirect('/verDepartamento')  

def eliminarEmpleado(request,emp_no):
    empleado=Empleado.objects.get(emp_no=emp_no)
    empleado.delete()
    return redirect('/verEmpleado')

class ArticuloListView(ListView):
    model=Articulo
    template_name='articulos.html'
    def get_queryset(self):
        queryset=self.model.objects.all()
        return queryset
class ArticuloDetailView(DetailView):
    model=detalleArticulo
    template_name='detalleArticulos.html'
    def get_object(self):
        objeto=self.model.objects.get(detalle_no=self.kwargs['detalle_no'])
        return objeto
    
    








