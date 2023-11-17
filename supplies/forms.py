from django import forms
from .models import Supplies, SupplieStatus

#Models
class CreateSupplieForm(forms.ModelForm):
    class Meta:
        model = Supplies
        fields = ['week','day_assignment','month','driver','truck','trailer','capacity','type_supplie','port_supplier','turns']
        labels = {
            'week': 'Semana',
            'day_assignment': 'Dia',
            'month': 'Mes',
            'driver': 'Operador',
            'truck': 'Camión',
            'trailer': 'Remolque',
            'capacity': 'Capacidad',
            'type_supplie': 'Tipo de Insumo',
            'port_supplier': 'Proveedor',
            'turns': 'Turnos',
        }
        widgets = {
            'week': forms.NumberInput(attrs={'class': 'form-control'}),
            'day_assignment': forms.Select(attrs={'class': 'form-control'}),
            'month': forms.Select(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'truck': forms.Select(attrs={'class': 'form-control'}),
            'trailer': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'type_supplie': forms.Select(attrs={'class': 'form-control'}),
            'port_supplier': forms.Select(attrs={'class': 'form-control'}),
            'turns': forms.Select(attrs={'class': 'form-control'}),
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = SupplieStatus
        fields = '__all__'
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'coordinates': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DataSupplieForm(forms.ModelForm):
    class Meta:
        model = Supplies
        fields = '__all__'
        widgets = {
            'folio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SupplieTrafficForm(forms.ModelForm):
    class Meta:
        model = Supplies
        fields = ['total_kms','empty_kms','dead_kms','lts_diesel','performance','urea']
        labels ={
            'total_kms': 'Kilometros Totales',
            'empty_kms': 'Kilometros Vacios',
            'dead_kms': 'Kilometros Muertos',
            'lts_diesel': 'Litros de Diesel',
            'performance': 'Rendimiento',
            'urea':'Urea',
        }
        widgets ={
            'total_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'empty_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'dead_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'lts_diesel': forms.NumberInput(attrs={'class':'form-control'}),
            'performance': forms.NumberInput(attrs={'class':'form-control'}),
            'urea': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
'''class AssigmentSupplie(forms.ModelForm):
    class Meta:
        model = CreateAssignation
        fields = ['week','day_assignment','driver','truck','trailer','capacity','type_supplie', 'port_supplier', 'turns']
        labels = {
            'week': 'Semana',
            'day_assignment': 'Dia de Asignacion',
            'driver': 'Operador',
            'truck': 'Unidad',
            'trailer': 'Tolva',
            'capacity': 'Capacidad',
            'type_supplie': 'Tipo de Insumo',
            'port_supplier': 'Proveedor',
            'turns': 'Turnos',
        }
        widgets={
            'week': forms.NumberInput(attrs={'class': 'form-control'}),
            'day_assignment': forms.Select(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'truck': forms.Select(attrs={'class': 'form-control'}),
            'trailer': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'type_supplie': forms.Select(attrs={'class': 'form-control'}),
            'port_supplier': forms.Select(attrs={'class': 'form-control'}),
            'turns': forms.TextInput(attrs={'class': 'form-control'}),
        }'''
    
class BillingForm(forms.ModelForm):
    class Meta: 
        model= Supplies
        fields = ['fact_cp','date_fact','unit_price','amount']
        widgets={
            'fact_cp': forms.TextInput(attrs={'class':'form-control'}),
            'date_fact': forms.DateInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class':'form-control'}),
        }

class SearchFolio(forms.Form):
    folio = forms.IntegerField(label='Número de Folio', widget=forms.NumberInput(attrs={'min': 0}))

        