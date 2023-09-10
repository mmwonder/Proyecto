from django.urls import path
from simpleCRUD.views import insertar,modificar,eliminar,ProductoInsertarView

urlpatterns = [
    path('insertar/<int:numprod>',insertar),
    path('modificar/<int:numprod>',modificar),
    path('eliminar/<int:numprod>',eliminar),
    path('insertarCreateView',ProductoInsertarView.as_view())
]