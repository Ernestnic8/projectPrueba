from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='inicio'),
    path('empleado', views.empleados, name='empleado'),
    path('empleado/crear',views.crearEmpleados, name="crear"),
    path('empleado/editar',views.editarEmpleados, name="editar"),
    path('empleado/eliminar/<int:empleadoid>', views.eliminarEmpleado, name='eliminar'),
    path('empleado/editar/<int:empleadoid>', views.editarEmpleados, name='editar'),

    path('libro', views.libros, name='libro'),
    path('libro/crear',views.crearLibro, name="crearLibro"),
    path('libro/editar',views.editarLibro, name="editarLibro"),
    path('libro/eliminar/<int:id>', views.eliminarLibro, name='eliminarLibro'),
    path('libro/editar/<int:id>', views.editarLibro, name='editarLibro'),

    path('cliente', views.cliente, name='cliente'),
    path('cliente/crear',views.crearCliente, name="crearCliente"),
    path('cliente/editar',views.editarCliente, name="editarCliente"),
    path('cliente/eliminar/<int:id>', views.eliminarCliente, name='eliminarCliente'),
    path('cliente/editar/<int:id>', views.editarCliente, name='editarCliente'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)