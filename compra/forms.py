from django import forms
from .models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']

class ProductoForm(forms.ModelForm):
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all())
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'proveedor']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['proveedor'].choices = [(proveedor.nombre) for proveedor in Proveedor.objects.all()]