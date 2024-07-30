from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleados, Libro, Clientes
from .forms import EmpleadoForm, LibroForm, ClienteForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'Empleado/index.html', {'empleados': empleados})

def crearEmpleados(request):
    formulario = EmpleadoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('empleado')
    return render(request, 'Empleado/crear.html', {'formulario': formulario})

def editarEmpleados(request, empleadoid):
    empleados = get_object_or_404(Empleados, empleadoid=empleadoid)
    formulario = EmpleadoForm(request.POST or None, instance=empleados)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('empleado')
    return render(request, 'Empleado/editar.html', {'formulario': formulario})

def eliminarEmpleado(request, empleadoid):
    empleados = get_object_or_404(Empleados, empleadoid=empleadoid)
    empleados.delete()
    return redirect('empleado')


def libros(request):
    libros = Libro.objects.all()
    return render(request, 'Libro/index.html', {'libros': libros})

def crearLibro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libro')
    return render(request, 'Libro/crear.html', {'formulario': formulario})

def editarLibro(request, id):
    libro = get_object_or_404(Libro, libroid=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libro')
    return render(request, 'Libro/editar.html', {'formulario': formulario})

def eliminarLibro(request, id):
    libro = get_object_or_404(Libro, libroid=id)
    libro.delete()
    return redirect('libro')

def cliente(request):
    clientes = Clientes.objects.all()
    return render(request, 'Cliente/index.html', {'clientes': clientes})

def crearCliente(request):
    formulario = ClienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cliente')
    return render(request, 'Cliente/crear.html', {'formulario': formulario})

def editarCliente(request, id):
    cliente = get_object_or_404(Clientes, clienteid=id)
    formulario = ClienteForm(request.POST or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cliente')
    return render(request, 'Cliente/editar.html', {'formulario': formulario})

def eliminarCliente(request, id):
    cliente = get_object_or_404(Clientes, clienteid=id)
    cliente.delete()
    return redirect('cliente')