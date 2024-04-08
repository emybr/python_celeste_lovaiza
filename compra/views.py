from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm

#Crear proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

#Crear producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

#Listar todos los proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

#Listar todos los productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})