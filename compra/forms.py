# from django import forms
# from .models import Proveedor, Producto

# class ProveedorForm(forms.ModelForm):
#     class Meta:
#         model = Proveedor
#         fields = ['nombre', 'apellido', 'dni']

# class ProductoForm(forms.ModelForm):
#     proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all())
#     class Meta:
#         model = Producto
#         fields = ['nombre', 'precio', 'stock', 'proveedor']

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['proveedor'].choices = [(proveedor.nombre) for proveedor in Proveedor.objects.all()]


from django import forms
from .models import Proveedor, Producto

class ProductoForm(forms.ModelForm):
    proveedor = forms.ModelChoiceField(queryset=None)  # Definir el queryset en el constructor
    
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'proveedor']

    def __init__(self, *args, **kwargs):
        initial_proveedor_choices = kwargs.pop('proveedor_choices', None)  # Obtener proveedor_choices del kwargs
        super().__init__(*args, **kwargs)
        if initial_proveedor_choices is not None:
            self.fields['proveedor'].queryset = initial_proveedor_choices

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']