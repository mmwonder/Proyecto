from django.shortcuts import redirect
from ventasApp.models import Producto
from django.views.generic import CreateView

# Create your views here.

def insertar(request,numprod):
    p=Producto(producto_no=numprod,descripcion="elemento a eliminar",precio_actual=87.50,stock_disponible=25)
    p.save()
    return redirect('/') 

class ProductoInsertarView(CreateView):
    model=Producto
    fields=["producto_no","descripcion","precio_actual","stock_disponible"]
    
def modificar(request,numprod):
    p=Producto(producto_no=numprod)
    p.descripcion="hemos cambiado este campo"
    p.save()
    return redirect('/')
def eliminar(request,numprod):
    p=Producto(producto_no=numprod)
    p.delete()
    return redirect('/')