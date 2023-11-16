from django import forms
from .models import Trips, IdConcept, MonthExpenses, Route, RoutePoint
from django.forms.widgets import DateInput, TimeInput
from django.utils import timezone


class CustomDateInput(DateInput):
    input_type = 'date'
    attrs = {'class': 'form-control flatpickr'}

class CustomTimeInput(TimeInput):
    input_type = 'time'
    attrs = {'class': 'form-control flatpickr timepicker'}

class CreateTripForm(forms.ModelForm):
    serv_date = forms.DateField(widget=CustomDateInput)
    class Meta:
        model = Trips
        fields = ['lote','weight','type_service','week','month','serv_date','supplier','oigin','meeting_place','meeting_hour','truck','trailer','driver','route']
        labels = {
            'lote': 'Número de Lote',
            'weight': 'Pesada',
            'type_service': 'Tipo de Servicio',
            'week': 'Semana',
            'month': 'Mes',
            'serv_date': 'Fecha de Servicio',
            'supplier': 'Acopiador',
            'oigin': 'Origen',
            'meeting_place': 'Lugar de Cita',
            'meeting_hour': 'Hora de Cita',
            'truck': 'Camión',
            'trailer': 'Remolque',
            'driver': 'Conductor',
            'route':'Ruta',
        }
        widgets = {
            'lote': forms.NumberInput(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'type_service': forms.Select(attrs={'class':'form-control'}),
            'week': forms.NumberInput(attrs={'class':'form-control'}),
            'month': forms.Select(attrs={'class':'form-control'}),
            'serv_date': CustomDateInput(attrs={'class':'form-control'}),
            'supplier': forms.Select(attrs={'class':'form-control'}),
            'oigin': forms.Select(attrs={'class':'form-control'}),
            'meeting_place': forms.TextInput(attrs={'class':'form-control'}),
            'meeting_hour': CustomTimeInput(attrs={'class':'form-control'}),
            'truck': forms.Select(attrs={'class':'form-control'}),
            'trailer': forms.Select(attrs={'class':'form-control'}),
            'driver': forms.Select(attrs={'class':'form-control'}),
            'route': forms.HiddenInput(),
        }
        
def __init__(self, *args, **kwargs):
    super(CreateTripForm, self).__init__(*args, **kwargs)
    self.fields['route'].choices = [(route.id, route.name) for route in Route.objects.all()]



#Horarios de Viaje
class RanchExit(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['ranch_exit','kms_exit']
        labels = {
            'ranch_exit': 'Salida de Rancho',
            'kms_exit': 'Kilómetros de Salia',
        }
        widgets = {
            'ranch_exit': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'kms_exit': forms.NumberInput(attrs={'class':'form-control'}),
        }    

class ArrivePoint(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['arrive_point','arrive_kms']
        labels = {
            'arrive_point': 'Punto de Llegada',
            'arrive_kms': 'Kilómetros de Llegada a Cita',
        }
        widgets = {
            'arrive_point': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'arrive_kms': forms.NumberInput(attrs={'class':'form-control'}),
        }

class ArriveSupplier(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['arrive_supp','arrive_kmssupp']
        labels = {
            'arrive_supp': 'Llegada al acopio',
            'arrive_kmssupp': 'Kilometros de llegada a acopio',
        }
        widgets = {
            'arrive_supp': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'arrive_kmssupp': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Cargo1(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['cargo1_kms','cargo1_site','cargo1_collected','cargo1_coordinates']
        widgets = {
            'cargo1_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo1_site': forms.TextInput(attrs={'class':'form-control'}),
            'cargo1_collected': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Cargo2(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['cargo2_kms','cargo2_site','cargo2_collected','cargo2_coordinates']
        labels = {
            'cargo2_kms': 'Kilómetros de Carga 2',
            'cargo2_site': 'Sitio de Carga 2',
            'cargo2_collected': 'Carga 2 Recogida',
        }
        widgets = {
            'cargo2_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo2_site': forms.TextInput(attrs={'class':'form-control'}),
            'cargo2_collected': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
class Cargo3(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['cargo3_kms','cargo3_site','cargo3_collected','cargo3_coordinates']
        labels = {
            'cargo3_kms': 'Kilómetros de Carga 3',
            'cargo3_site': 'Sitio de Carga 3',
            'cargo3_collected': 'Carga 3 Recogida',
        }
        widgets = {
            'cargo3_kms': forms.TextInput(attrs={'class':'form-control'}),
            'cargo3_site': forms.TextInput(attrs={'class':'form-control'}),
            'cargo3_collected': forms.NumberInput(attrs={'class':'form-control'}),
        }

class ExitSupplier(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['exit_supplier','exit_supplierkms']
        labels = {
            'exit_supplier': 'Salida del Proveedor',
            'exit_supplierkms':'Kilometros salida Proveedor',
        }
        widgets = {
            'exit_supplier': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'exit_supplierkms': forms.NumberInput(attrs={'class':'form-control'}),
        }

class ArriveRanch(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['ranch_arrive','ranch_kms']
        labels = {
            'ranch_arrive': 'Llegada a Rancho',
            'ranch_kms': 'Kilómetros a Rancho',
        }
        widgets = {
            'ranch_arrive': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'ranch_kms': forms.NumberInput(attrs={'class':'form-control'}),
        }

class FormAll(forms.ModelForm):
    class Meta:
        model = Trips
        fields = '__all__'

class TravelDataForm(forms.ModelForm):
    ranch_exit = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
        initial=timezone.now(),
    )
    class Meta:
        model = Trips
        fields = ['ranch_exit','kms_exit','arrive_point','arrive_kms','arrive_supp','arrive_kmssupp','cargo1_arrival','cargo1_kms','cargo1_site','cargo1_collected','cargo1_fin','cargo2_arrival','cargo2_kms','cargo2_site','cargo2_collected','cargo2_fin','cargo3_arrival','cargo3_kms','cargo3_site','cargo3_collected','cargo3_fin','exit_supplier','exit_supplierkms','comentaries','ranch_arrive','ranch_kms']
        labels = {
            'ranch_exit': 'Salida de Rancho',
            'kms_exit': 'Kilómetros de Salia',
            'arrive_point': 'Punto de Llegada',
            'arrive_kms': 'Kilómetros de Llegada a Cita',
            'arrive_supp': 'Llegada al acopio',
            'arrive_kmssupp': 'Kilometros de llegada a acopio',
            'cargo1_arrival': 'Llegada de Carga 1',
            'cargo1_kms': 'Kilómetros de Carga 1',
            'cargo1_site': 'Sitio de Carga 1',
            'cargo1_collected': 'Carga 1 Recogida',
            'cargo1_fin': 'Finalización de Carga 1',
            'cargo2_arrival': 'Llegada de Carga 2',
            'cargo2_kms': 'Kilómetros de Carga 2',
            'cargo2_site': 'Sitio de Carga 2',
            'cargo2_collected': 'Carga 2 Recogida',
            'cargo2_fin': 'Finalización de Carga 2',
            'cargo3_arrival': 'Llegada de Carga 3',
            'cargo3_kms': 'Kilómetros de Carga 3',
            'cargo3_site': 'Sitio de Carga 3',
            'cargo3_collected': 'Carga 3 Recogida',
            'cargo3_fin': 'Finalización de Carga 3',
            'exit_supplier': 'Salida del Proveedor',
            'exit_supplierkms':'Kilometros salida Proveedor',
            'comentaries': 'Comentarios',
            'ranch_arrive': 'Llegada a Rancho',
            'ranch_kms': 'Kilómetros a Rancho',
        }
        widgets = {
            'ranch_exit': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'kms_exit': forms.NumberInput(attrs={'class':'form-control'}),
            'arrive_point': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'arrive_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'arrive_supp': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'arrive_kmssupp': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo1_arrival': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'cargo1_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo1_site': forms.TextInput(attrs={'class':'form-control'}),
            'cargo1_collected': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo1_fin': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'cargo2_arrival': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'cargo2_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo2_site': forms.TextInput(attrs={'class':'form-control'}),
            'cargo2_collected': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo2_fin': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'cargo3_arrival': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'cargo3_kms': forms.TextInput(attrs={'class':'form-control'}),
            'cargo3_site': forms.TextInput(attrs={'class':'form-control'}),
            'cargo3_collected': forms.NumberInput(attrs={'class':'form-control'}),
            'cargo3_fin': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'exit_supplier': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'exit_supplierkms': forms.NumberInput(attrs={'class':'form-control'}),
            'comentaries': forms.TextInput(attrs={'class':'form-control'}),
            'ranch_arrive': forms.DateTimeInput(attrs={'class': 'form-control flatpickr'}),
            'ranch_kms': forms.NumberInput(attrs={'class':'form-control'}),
        }

def render_ranch_exit(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-ranch_exit" name="{self.prefix}-ranch_exit">'

def render_arrive_point(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-arrive_point" name="{self.prefix}-arrive_point">'

def render_cargo1_arrival(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-cargo1_arrival" name="{self.prefix}-cargo1_arrival">'

def render_cargo1_fin(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-cargo1_fin" name="{self.prefix}-cargo1_fin">'

def render_cargo2_arrival(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-cargo2_arrival" name="{self.prefix}-cargo2_arrival">'

def render_cargo2_fin(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-cargo2_fin" name="{self.prefix}-cargo2_fin">'

def render_cargo3_arrival(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-cargo3_arrival" name="{self.prefix}-cargo3_arrival">'

def render_cargo3_fin(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-cargo3_fin" name="{self.prefix}-cargo3_fin">'

def render_exit_supplier(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-exit_supplier" name="{self.prefix}-exit_supplier">'

def render_ranch_arrive(self):
    return f'<input type="text" class="form-control flatpickr" id="{self.prefix}-ranch_arrive" name="{self.prefix}-ranch_arrive">'

class TraficDataForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['total_kms','empty_kms','dead_kms','lts_diesel','performance','urea']
        labels = {
            'total_kms': 'Kilómetros totales',
            'empty_kms': 'Kilómetros vacíos',
            'dead_kms': 'Kilómetros muertos',
            'lts_diesel': 'Litros de diésel',
            'performance': 'Rendimiento (km/l)',
            'urea': 'Urea',
        }
        widgets = {
            'total_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'empty_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'dead_kms': forms.NumberInput(attrs={'class':'form-control'}),
            'lts_diesel': forms.NumberInput(attrs={'class':'form-control'}),
            'performance': forms.NumberInput(attrs={'class':'form-control'}),
            'urea': forms.NumberInput(attrs={'class':'form-control'}),
        }

class TravelExpencesForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['stand','iave','food','dessinfections','fixes','parts','tires','pension','federal']
        labels = {
            'stand': 'Caseta',
            'iave': 'IAVE',
            'food': 'Comida',
            'dessinfections': 'Desinfecciones',
            'fixes': 'Reparaciones',
            'parts': 'Partes',
            'tires': 'Llantas',
            'pension': 'Pensión',
            'federal': 'Federales',
        }
        widgets = {
            'stand': forms.NumberInput(attrs={'class':'form-control'}),
            'iave': forms.NumberInput(attrs={'class':'form-control'}),
            'food': forms.NumberInput(attrs={'class':'form-control'}),
            'dessinfections': forms.NumberInput(attrs={'class':'form-control'}),
            'fixes': forms.NumberInput(attrs={'class':'form-control'}),
            'parts': forms.NumberInput(attrs={'class':'form-control'}),
            'tires': forms.NumberInput(attrs={'class':'form-control'}),
            'pension': forms.NumberInput(attrs={'class':'form-control'}),
            'federal': forms.NumberInput(attrs={'class':'form-control'}),
        }

class BillinForm(forms.ModelForm):
    class Meta: 
        model= Trips
        fields = ['type_fact','fact_cp','date_fact','amount','unit_price','type_note','amount_note']
        labels= {
            'type_fact': 'Tipo de factura',
            'fact_cp': 'Folio de factura',
            'date_fact':'Fecha de factura',
            'amount':'Cantidad Facturada',
            'unit_price':'Precio unitario',
            'type_note':'Tipo de nota',
            'amount_note':'Monto de la nota',
        }
        widgets={
            'type_fact': forms.Select(attrs={'class':'form-control'}),
            'fact_cp': forms.NumberInput(attrs={'class':'form-control'}),
            'date_fact': forms.NumberInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class':'form-control'}),
            'type_note': forms.Select(attrs={'class':'form-control'}),
            'amount_note': forms.NumberInput(attrs={'class':'form-control'}),
        }

class ExpensesMonth(forms.ModelForm):
    class Meta:
        model = MonthExpenses
        fields = '__all__'
        widgets = {
            'month': forms.Select(attrs={'class': 'form-control'}),  # Esto especifica que se usará un campo de selección
        }
        
class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name_route', 'desc_route']

class RoutePointForm(forms.ModelForm):
    class Meta:
        model = RoutePoint
        fields = ['route', 'lat_route', 'lon_route']
        widgets = {
            'route': forms.HiddenInput(),
            'lat_route': forms.HiddenInput(),
            'lon_route': forms.HiddenInput(),
        }