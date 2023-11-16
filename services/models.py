from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class Address(models.Model):
    id_address=models.AutoField(primary_key=True)
    address_supplier=models.CharField(max_length=100)

class Origin(models.Model):
    id_origin=models.AutoField(primary_key=True)
    name_origin=models.CharField(max_length=20)
    state_origin=models.CharField(max_length=20)
    min_time=models.TimeField()
    max_time=models.TimeField()
    def __str__(self):
        return self.name_origin

class Month(models.Model):
    id_month=models.AutoField(primary_key=True)
    name_month=models.CharField(max_length=15)
    def __str__(self):
        return self.name_month

class ServiceType(models.Model):
    id_tipe=models.AutoField(primary_key=True)
    name_type=models.CharField(max_length=15)
    def __str__(self):
        return self.name_type

class Supplier(models.Model):
    id_suppler=models.AutoField(primary_key=True)
    name_supplier=models.CharField(max_length=80)
    def __str__(self):
        return self.name_supplier

class Truck(models.Model):
    id_truck=models.AutoField(primary_key=True)
    truck_num=models.CharField(max_length=4)
    plate=models.CharField(max_length=10)
    year=models.CharField(max_length=4)
    vin=models.CharField(max_length=25)
    trademark=models.CharField(max_length=15)
    assured=models.CharField(max_length=20)
    def __str__(self):
        return self.truck_num
    
class Driver(models.Model):
    id_driver=models.AutoField(primary_key=True)
    name_driver=models.CharField(max_length=35)
    celphone=models.IntegerField()
    address=models.TextField(max_length=100)
    e_mail=models.CharField(max_length=30)
    def __str__(self):
        return self.name_driver

class Trailer(models.Model):
    id_trailer=models.AutoField(primary_key=True)
    trailer_num=models.CharField(max_length=4)
    plate=models.CharField(max_length=10)
    year=models.CharField(max_length=4)
    vin=models.CharField(max_length=25)
    trademark=models.CharField(max_length=15)
    assured=models.CharField(max_length=20)
    def __str__(self):
        return self.trailer_num
    
class type_fact(models.Model):
    id_typef=models.AutoField(primary_key=True)
    type_namef=models.CharField(max_length=8, null=True)
    def __str__(self):
        return self.type_namef
    
class type_note(models.Model):
    id_typen=models.AutoField(primary_key=True)
    type_namen=models.CharField(max_length=8, null=True)
    def __str__(self):
        return self.type_namen

class Route(models.Model):
    id_route = models.AutoField(primary_key=True)
    name_route = models.CharField(max_length=150)
    desc_route = models.CharField(max_length=300)
    def __str__(self):
        return 'Ruta: ' + self.name_route + ', Descripción: ' + self.desc_route

class RoutePoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    lat_route = models.DecimalField(max_digits=9, decimal_places=6)
    lon_route = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return f'{self.route.name_route}, lat: {self.lat_route}, lon: {self.lon_route}'
        
class Trips(models.Model):
    id_service = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, db_column='Creacion')
    lote = models.IntegerField(null=True, blank=True, db_column='Número de Lote')
    week = models.CharField(max_length=2, null=True, blank=True, db_column='Semana')
    weight = models.IntegerField(null=True, blank=True, db_column='Peso')
    type_service = models.ForeignKey(ServiceType, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Tipo de Servicio')
    month = models.ForeignKey(Month, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Mes')
    serv_date = models.DateField(null=True, blank=True, db_column='Fecha de Servicio')
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Proveedor')
    oigin = models.ForeignKey(Origin, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Origen')
    meeting_place = models.CharField(max_length=50, null=True, blank=True, db_column='Lugar de Encuentro')
    meeting_hour = models.TimeField(null=True, blank=True, db_column='Hora de Encuentro')
    truck = models.ForeignKey(Truck, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Camión')
    truck_plates = models.ForeignKey(Truck, related_name='assignations_with_truck_plates', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Placas de Camión')
    trailer = models.ForeignKey(Trailer, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Remolque')
    trailer_plates = models.ForeignKey(Trailer, related_name='assignations_with_trailer_plates', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Placas de Remolque')
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Conductor')
    route = models.ForeignKey(Route, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Ruta')
    #DATOS DE VIAJE
    ranch_exit = models.DateTimeField(null=True, blank=True, db_column='Salida de Rancho')
    kms_exit = models.IntegerField(null=True, blank=True, db_column='Kilómetros de Salida')
    arrive_point = models.DateTimeField(null=True, blank=True, db_column='Punto de Llegada')
    arrive_kms = models.IntegerField(null=True, blank=True, db_column='Kilómetros de Llegada a Cita')
    arrive_supp = models.DateTimeField(null=True, blank=True, db_column='Legada al acopio')
    arrive_kmssupp = models.IntegerField(null=True, blank=True, db_column='Kilómetros de Llegada al acopio')
    cargo1_arrival = models.DateTimeField(null=True, blank=True, db_column='Llegada de Carga 1')
    cargo1_kms = models.IntegerField(null=True, blank=True, db_column='Kilómetros de Carga 1')
    cargo1_site = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='trips_cargo1', related_query_name='trip_cargo1', db_column='Sitio de Carga 1')
    cargo1_collected = models.IntegerField(null=True, blank=True, db_column='Carga 1 Recogida')
    cargo1_fin = models.DateTimeField(null=True, blank=True, db_column='Finalización de Carga 1')
    cargo1_coordinates = models.CharField(max_length=50, null=True, blank=True, db_column='Coordenadas 1')
    cargo2_arrival = models.DateTimeField(null=True, blank=True, db_column='Llegada de Carga 2')
    cargo2_kms = models.IntegerField(null=True, blank=True, db_column='Kilómetros de Carga 2')
    cargo2_site = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='trips_cargo2', related_query_name='trip_cargo2', db_column='Sitio de Carga 2')
    cargo2_collected = models.IntegerField(null=True, blank=True, db_column='Carga 2 Recogida')
    cargo2_fin = models.DateTimeField(null=True, blank=True, db_column='Finalización de Carga 2')
    cargo2_coordinates = models.CharField(max_length=50, null=True, blank=True, db_column='Coordenadas 2')
    cargo3_arrival = models.DateTimeField(null=True, blank=True, db_column='Llegada de Carga 3')
    cargo3_kms = models.IntegerField(null=True, blank=True, db_column='Kilómetros de Carga 3')
    cargo3_site = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='trips_cargo3', related_query_name='trip_cargo3', db_column='Sitio de Carga 3')
    cargo3_collected = models.IntegerField(null=True, blank=True, db_column='Carga 3 Recogida')
    cargo3_fin = models.DateTimeField(null=True, blank=True, db_column='Finalización de Carga 3')
    cargo3_coordinates = models.CharField(max_length=50, null=True, blank=True, db_column='Coordenadas 3')
    exit_supplier = models.DateTimeField(null=True, blank=True, db_column='Salida de Proveedor')
    exit_supplierkms = models.IntegerField(null=True, blank=True, db_column='Kilómetros salida Proveedor')
    comentaries = models.TextField(max_length=200, null=True, blank=True, db_column='Comentarios')
    ranch_arrive = models.DateTimeField(null=True, blank=True, db_column='Llegada a Rancho')
    ranch_kms = models.IntegerField(null=True, blank=True, db_column='Kilómetros a Rancho')
    #DATOS DE TRAFICO
    total_collected = models.IntegerField(null=True, blank=True, db_column='Total Recogido')
    total_kms = models.IntegerField(null=True, blank=True, db_column='Total de Kilómetros')
    empty_kms = models.IntegerField(null=True, blank=True, db_column='Kilómetros Vacíos')
    dead_kms = models.IntegerField(null=True, blank=True, db_column='Kilómetros Muertos')
    lts_diesel = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Litros de Diesel')
    performance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Rendimiento')
    urea = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Urea')
    #GASTOS
    stand = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Stand')
    iave = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='IAVE')
    food = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Comida')
    dessinfections = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Desinfecciones')
    fixes = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Reparaciones')
    parts = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Partes')
    tires = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Llantas')
    pension = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Pensión')
    federal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Federal')
    #FACTURACION
    type_fact = models.ForeignKey(type_fact, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Tipo de Factura')
    fact_cp = models.CharField(max_length=8, null=True, blank=True, db_column='Código Postal de Factura')
    date_fact = models.DateTimeField(null=True, blank=True, db_column='Fecha de Factura')
    amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Monto')
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Precio Unitario')
    type_note = models.ForeignKey(type_note, on_delete=models.DO_NOTHING, null=True, blank=True, db_column='Tipo de Nota')
    amount_note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Monto de Nota')
    def __str__(self):
        return 'LOTE #: ' + str(self.lote) + ' ' + str(self.type_service)
    
    def save(self, *args, **kwargs):
        if self.truck:
            truck_instance = Truck.objects.get(truck_num=self.truck.truck_num)
            self.truck_plates = truck_instance
        if self.trailer:
            trailer_instance = Trailer.objects.get(trailer_num=self.trailer.trailer_num)
            self.trailer_plates = trailer_instance
        super(Trips, self).save(*args, **kwargs)
        
@receiver(pre_save, sender=Trips)
def calcular_total_collected(sender, instance, **kwargs):
    total_collected = (instance.cargo1_collected or 0) + (instance.cargo2_collected or 0) + (instance.cargo3_collected or 0)
    instance.total_collected = total_collected

@receiver(pre_save, sender=Trips)
def calcular_kms_difference(sender, instance, **kwargs):
    if instance.kms_exit is not None and instance.arrive_kms is not None:
        instance.empty_kms = instance.arrive_kms - instance.kms_exit
    else:
        instance.empty_kms = None

@receiver(pre_save, sender=Trips)        
def calcular_kms_difference(sender, instance, **kwargs):
    if instance.kms_exit is not None and instance.ranch_kms is not None:
        instance.total_kms = instance.ranch_kms - instance.kms_exit
    else:
        instance.total_kms = None

@receiver(pre_save, sender=Trips)
def calculate_performance(sender, instance, **kwargs):
    if instance.lts_diesel is not None and instance.total_kms is not None:
        if instance.total_kms != 0:
            instance.performance = instance.lts_diesel / instance.total_kms
    else:
        instance.performance = None

class IdConcept(models.Model):
    id_concept = models.AutoField(primary_key=True)
    name_concept = models.CharField(max_length=50)
    def __str__(self):
        return self.name_concept
        
class MonthExpenses(models.Model):
    id_expenses =models.AutoField(primary_key=True)
    month = models.ForeignKey(Month, on_delete=models.DO_NOTHING, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    name_conceptt = models.ForeignKey(IdConcept, on_delete=models.DO_NOTHING )
    total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    expense_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    proportional_trip = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    proportional_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
