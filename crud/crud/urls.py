"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ventasApp.views import inicio,ProductoListView,DepartamentoListView,EmpleadoListView,EmpleadoDetailView,ArticuloListView,ArticuloDetailView,insertarProducto,eliminarProducto,insertarDepartamento,eliminarDepartamento,insertarEmpleado,eliminarEmpleado,modificarDepartamento
#DepartamentoModificarFormView,modificarDepartamento
from carritoApp.views import agregar_producto, eliminar_producto, limpiar_carrito, restar_producto, tienda
from simpleCRUD import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
    path('tienda/',tienda,name="Tienda"),
    path('agregar/<int:producto_id>',agregar_producto,name="Add"),
    path('eliminar/<int:producto_id>',eliminar_producto,name="Del"),
    path('sacar/<int:producto_id>',restar_producto,name="Sub"),
    path('limpiar/',limpiar_carrito,name="Cls"),
    path('verProducto',ProductoListView.as_view()),
    path('verDepartamento',DepartamentoListView.as_view(), name='departamento-base'),
    path('verEmpleado',EmpleadoListView.as_view()),
    path('verTienda',ArticuloListView.as_view()),
    path('insertarProducto',insertarProducto),
    path('insertarDepartamento',insertarDepartamento),
    path('detalleDepartamento/<int:depto_no>',EmpleadoDetailView.as_view()),
    path('modificarDepartamento/<pk>',modificarDepartamento.as_view()),
    #path('modificarDepartamento',DepartamentoModificarFormView.as_view()),
    path('detalleArticulo/<int:detalle_no>',ArticuloDetailView.as_view()),
    path('insertarEmpleado',insertarEmpleado),
    path('eliminarProducto/<int:prod_no>',eliminarProducto),
    path('eliminarDepartamento/<int:dep_no>',eliminarDepartamento),
    path('eliminarEmpleado/<int:emp_no>',eliminarEmpleado),
    path('aplicacion/',include('simpleCRUD.urls'))
]
    
    
