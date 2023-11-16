from django.db import models
from services.models import Month, Driver, Truck, Trailer


# Create your models here.
class Turn(models.Model):
    id_turn=models.AutoField(primary_key=True)
    turn=models.CharField(max_length=10)
    def __str__(self):
        return self.turn

class Status(models.Model):
    id_status=models.AutoField(primary_key=True)
    status=models.CharField(max_length=30)
    def __str__(self):
        return self.status

class PortSupplier(models.Model):
    id_status=models.AutoField(primary_key=True)
    port_supplier=models.CharField(max_length=30)
    def __str__(self):
        return self.port_supplier

class TypeSupplie(models.Model):
    id_supplie = models.AutoField(primary_key=True)
    name_supplie = models.CharField(max_length=10)
    def __str__(self):
        return self.name_supplie

class ConditionStatus(models.Model):
    id_condition=models.AutoField(primary_key=True)
    condition_status=models.CharField(max_length=50)
    def __str__(self):
        return self.condition_status

class WeekDays(models.Model):
    id_day=models.AutoField(primary_key=True)
    name_day=models.CharField(max_length=15)
    def __str__(self):
        return self.name_day
         
'''class Supplies(models.Model):
    id_serv=models.AutoField(primary_key=True)
    created=models.DateTimeField(auto_now_add=True)
    folio=models.IntegerField(null=True, blank=True)
    week=models.IntegerField(null=True, blank=True)
    day_assignment=models.ForeignKey(WeekDays, on_delete=models.DO_NOTHING, null=True)
    driver=models.ForeignKey(Driver, on_delete=models.DO_NOTHING,null=True,  blank=True)
    truck=models.ForeignKey(Truck, on_delete=models.DO_NOTHING,null=True,  blank=True)
    truck_plate=models.ForeignKey(Truck,related_name='assignations_with_truck_plate', on_delete=models.DO_NOTHING, null=True, blank=True)
    trailer=models.ForeignKey(Trailer, on_delete=models.DO_NOTHING,null=True,  blank=True)
    trailer_plate=models.ForeignKey(Trailer, related_name='assignations_with_trailer_plate', on_delete=models.DO_NOTHING,null=True, blank=True)
    capacity=models.CharField(max_length=10, null=True)
    type_supplie=models.ForeignKey(TypeSupplie, on_delete=models.DO_NOTHING,null=True, blank=True)
    month=models.ForeignKey(Month, on_delete=models.DO_NOTHING, null=True, blank=True)
    serv_date=models.DateField(null=True, blank=True)
    port_supplier=models.ForeignKey(PortSupplier, on_delete=models.DO_NOTHING,null=True,  blank=True)
    turns=models.CharField(max_length=15, null=True)
    #HORARIOS DE CARGA DE VIAJE
    ranch_exitd=models.DateField(null=True, blank=True)
    ranch_exith=models.TimeField(null=True, blank=True)
    kms_exit=models.IntegerField(null=True, blank=True)
    calt_date=models.DateField(null=True, blank=True)
    calt_hour=models.TimeField(null=True, blank=True)
    date_arrives=models.DateField(null=True, blank=True)
    hour_arrives=models.TimeField(null=True, blank=True)
    initc_date=models.DateField(null=True, blank=True)
    initchar_hour=models.TimeField(null=True, blank=True)
    endchar_date=models.DateField(null=True, blank=True)
    endchar_hour=models.TimeField(null=True, blank=True)
    exitport_date=models.DateField(null=True, blank=True)
    exitport_hour=models.TimeField(null=True, blank=True)
    arriver_date=models.DateField(null=True, blank=True)
    arriver_hour=models.TimeField(null=True, blank=True)
    initdown_date=models.DateField(null=True, blank=True)
    initdown_hour=models.TimeField(null=True, blank=True)
    enddown_date=models.DateField(null=True, blank=True)
    enddown_hour=models.TimeField(null=True, blank=True)
    emptyranch_date=models.DateField(null=True, blank=True)
    emptyranch_hour=models.TimeField(null=True, blank=True)
    #DATOS DE TRAFICO
    total_kms=models.IntegerField(null=True, blank=True)
    empty_kms=models.IntegerField(null=True, blank=True)
    dead_kms=models.IntegerField(null=True, blank=True)
    lts_diesel=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    performance=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    urea=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    #DATOS DE FACTURACION
    fact_cp=models.CharField(max_length=8, null=True, blank=True)
    date_fact=models.DateTimeField(null=True, blank=True)
    unit_price=models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    amount=models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    
    
    
    def save(self, *args, **kwargs):
        if self.truck:
            truck_instance = Truck.objects.get(truck_num=self.truck.truck_num)  # Obtener la instancia de Truck por número de unidad
            self.truck_plate = truck_instance  # Asignar la instancia de Truck a truck_plates
        if self.trailer:
            trailer_instance = Trailer.objects.get(trailer_num=self.trailer.trailer_num)  # Obtener la instancia de Trailer por número de trailer
            self.trailer_plate = trailer_instance  # Asignar la instancia de Trailer a trailer_plates
        super(Supplies, self).save(*args, **kwargs)

class SupplieStatus(models.Model):
    id = models.AutoField(primary_key=True)
    time_status = models.DateTimeField(auto_now_add=True)
    time_consult= models.DateTimeField(null=True, blank=True)
    time_dif=models.DurationField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    unit = models.ForeignKey(Truck, on_delete=models.DO_NOTHING)
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    turn = models.ForeignKey(Turn, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(PortSupplier, on_delete=models.DO_NOTHING)
    condition = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        formatted_time = self.time_consult.strftime('%Y-%m-%d %H:%M:%S')
        unit_number = self.unit.truck_num if self.unit else 'N/A'
        return f'{formatted_time} - {self.status} - Unit {unit_number}'
    
    def save(self, *args, **kwargs):
        if not self.id:  # Solo si es un nuevo registro
            last_status = SupplieStatus.objects.filter(unit=self.unit).last()
            if last_status:
                if self.time_status:
                    self.time_dif = self.time_status - last_status.time_status
                    last_status.time_consult = self.time_status
                    last_status.save()
            else:
                self.time_dif = None

        super(SupplieStatus, self).save(*args, **kwargs)'''
    
'''class CreateAssignation(models.Model):
    id_assignment=models.AutoField(primary_key=True)
    date_assignment=models.DateTimeField(auto_now_add=True)
    week=models.IntegerField()
    day_assignment=models.ForeignKey(WeekDays, on_delete=models.DO_NOTHING)
    driver=models.ForeignKey(Driver,on_delete=models.DO_NOTHING)
    truck=models.ForeignKey(Truck,on_delete=models.DO_NOTHING)
    truck_plates=models.ForeignKey(Truck,related_name='assignations_with_truck_plates', on_delete=models.DO_NOTHING)
    trailer=models.ForeignKey(Trailer,on_delete=models.DO_NOTHING)
    trailer_plates=models.ForeignKey(Trailer, related_name='assignations_with_trailer_plates', on_delete=models.DO_NOTHING)
    capacity=models.CharField(max_length=10)
    type_supplie=models.ForeignKey(TypeSupplie, on_delete=models.DO_NOTHING)
    port_supplier=models.ForeignKey(PortSupplier,null=True, on_delete=models.DO_NOTHING)
    turns=models.CharField(max_length=15)
        
    def save(self, *args, **kwargs):
        if self.truck:
            truck_instance = Truck.objects.get(truck_num=self.truck.truck_num)  # Obtener la instancia de Truck por número de unidad
            self.truck_plates = truck_instance  # Asignar la instancia de Truck a truck_plates
        if self.trailer:
            trailer_instance = Trailer.objects.get(trailer_num=self.trailer.trailer_num)  # Obtener la instancia de Trailer por número de trailer
            self.trailer_plates = trailer_instance  # Asignar la instancia de Trailer a trailer_plates
        super(CreateAssignation, self).save(*args, **kwargs)'''

class Supplies(models.Model):
    id_serv=models.AutoField(primary_key=True)
    created=models.DateTimeField(auto_now_add=True)
    folio=models.IntegerField(null=True, blank=True)
    week=models.IntegerField(null=True, blank=True)
    day_assignment=models.ForeignKey(WeekDays, on_delete=models.DO_NOTHING, null=True)
    driver=models.ForeignKey(Driver, on_delete=models.DO_NOTHING,null=True,  blank=True)
    truck=models.ForeignKey(Truck, on_delete=models.DO_NOTHING,null=True,  blank=True)
    truck_plate=models.ForeignKey(Truck,related_name='assignations_with_truck_plate', on_delete=models.DO_NOTHING, null=True, blank=True)
    trailer=models.ForeignKey(Trailer, on_delete=models.DO_NOTHING,null=True,  blank=True)
    trailer_plate=models.ForeignKey(Trailer, related_name='assignations_with_trailer_plate', on_delete=models.DO_NOTHING,null=True, blank=True)
    capacity=models.CharField(max_length=10, null=True)
    type_supplie=models.ForeignKey(TypeSupplie, on_delete=models.DO_NOTHING,null=True, blank=True)
    month=models.ForeignKey(Month, on_delete=models.DO_NOTHING, null=True, blank=True)
    serv_date=models.DateField(null=True, blank=True)
    port_supplier=models.ForeignKey(PortSupplier, on_delete=models.DO_NOTHING,null=True,  blank=True)
    turns=models.ForeignKey(Turn, on_delete=models.DO_NOTHING,null=True, blank=True)
    #HORARIOS DE CARGA DE VIAJE
    #------------->>>SALIDA DE RANCHO<<<-----------------
    status_exit = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='exit_ranch')
    ranch_exitd=models.DateTimeField(null=True, blank=True)
    ubi_exit=models.CharField(max_length=50, null=True, blank=True)
    kms_exit=models.IntegerField(null=True, blank=True)
    condition_exit = models.ForeignKey(ConditionStatus,on_delete=models.SET_NULL, null=True, blank=True, related_name='exit_condition')
    #------------->>>ACCESO A CALT<<<-----------------
    status_calt = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True,related_name='arriving_calt')
    calt_date=models.DateTimeField(null=True, blank=True)
    ubi_calt=models.CharField(max_length=50, null=True, blank=True)
    kms_calt=models.IntegerField(null=True, blank=True)
    condition_calt = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='calt_condition')
    #------------->>>INGRESO TERMINAL<<<-----------------
    status_arrive = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True,related_name='arriving_supplier')
    date_arrives=models.DateTimeField(null=True, blank=True)
    ubi_arrives=models.CharField(max_length=50, null=True, blank=True)
    kms_arrives=models.IntegerField(null=True, blank=True)
    condition_arrives = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='arrives_condition')
    #------------->>>iNICIO DE CARGA<<<-----------------
    status_initchar = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='init_char')
    initc_date=models.DateTimeField(null=True, blank=True)
    ubi_initchar=models.CharField(max_length=50, null=True, blank=True)
    kms_initchar=models.IntegerField(null=True, blank=True)
    condition_initchar = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='init_condition')
    #------------->>>FIN DE RANCHO<<<-----------------
    status_endchar = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='end_char')
    endchar_date=models.DateTimeField(null=True, blank=True)
    ubi_endchar=models.CharField(max_length=50, null=True, blank=True)
    kms_endchar=models.IntegerField(null=True, blank=True)
    condition_endchar = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True,related_name='end_condition')
    #------------->>>RUTAFISCAL<<<-----------------
    status_fiscal = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='fiscal')
    fiscal_date=models.DateTimeField(null=True, blank=True)
    ubi_fiscal=models.CharField(max_length=50, null=True, blank=True)
    kms_fiscal=models.IntegerField(null=True, blank=True)
    condition_fiscal = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='fiscal_condition')
    #------------->>>SALIDA DE RECINTO<<<-----------------
    status_exitport = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='exit_port')
    exitport_date=models.DateTimeField(null=True, blank=True)
    ubi_exitport=models.CharField(max_length=50, null=True, blank=True)
    kms_exitport=models.IntegerField(null=True, blank=True)
    condition_exitport = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True,related_name='exitport_condition')
    #------------->>>LLEGADA A RANCHO<<<-----------------
    status_arriver = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='arriving_ranch')
    arriver_date=models.DateTimeField(null=True, blank=True)
    ubi_arriver=models.CharField(max_length=50, null=True, blank=True)
    kms_arriver=models.IntegerField(null=True, blank=True)
    condition_arriver = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='erriver_condition')
    #------------->>>INICIO DE DESCARGA<<<-----------------
    status_initdown = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='init_down')
    initdown_date=models.DateTimeField(null=True, blank=True)
    ubi_initdown=models.CharField(max_length=50, null=True, blank=True)
    kms_initdown=models.IntegerField(null=True, blank=True)
    condition_initdown = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='initd_condition')
    #------------->>>TERMINO DE DESCARGA<<<-----------------
    status_enddown = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='end_down')
    enddown_date=models.DateTimeField(null=True, blank=True)
    ubi_enddown=models.CharField(max_length=50, null=True, blank=True)
    kms_enddown=models.IntegerField(null=True, blank=True)
    condition_enddown = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True,related_name='endd_condition')
    #------------->>>VACIO RANCHO<<<-----------------
    status_emptyranch = models.ForeignKey(Status, on_delete=models.DO_NOTHING,null=True, blank=True,related_name='empty_ranch')
    emptyranch_date=models.DateTimeField(null=True, blank=True)
    ubi_emptyranh=models.CharField(max_length=50, null=True, blank=True)
    kms_emptyranch=models.IntegerField(null=True, blank=True)
    condition_emptyranch = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='empty_condition')
    #DATOS DE TRAFICO
    total_kms=models.IntegerField(null=True, blank=True)
    empty_kms=models.IntegerField(null=True, blank=True)
    dead_kms=models.IntegerField(null=True, blank=True)
    lts_diesel=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    performance=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    urea=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #DATOS DE FACTURACION
    fact_cp=models.CharField(max_length=10, null=True, blank=True)
    date_fact=models.DateTimeField(null=True, blank=True)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    amount=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.truck:
            truck_instance = Truck.objects.get(truck_num=self.truck.truck_num)  # Obtener la instancia de Truck por número de unidad
            self.truck_plate = truck_instance  # Asignar la instancia de Truck a truck_plates
        if self.trailer:
            trailer_instance = Trailer.objects.get(trailer_num=self.trailer.trailer_num)  # Obtener la instancia de Trailer por número de trailer
            self.trailer_plate = trailer_instance  # Asignar la instancia de Trailer a trailer_plates
        super(Supplies, self).save(*args, **kwargs)

class SupplieStatus(models.Model):
    id = models.AutoField(primary_key=True)
    time_status = models.DateTimeField(auto_now_add=True)
    time_consult= models.DateTimeField(null=True, blank=True)
    time_dif=models.DurationField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    kms=models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    coordinates=models.CharField(max_length=50,null=True, blank=True)
    unit = models.ForeignKey(Truck,null=True, blank=True, on_delete=models.DO_NOTHING)
    driver = models.ForeignKey(Driver,null=True, blank=True, on_delete=models.DO_NOTHING)
    turn = models.ForeignKey(Turn,null=True, blank=True, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(PortSupplier,null=True, blank=True, on_delete=models.DO_NOTHING)
    condition = models.ForeignKey(ConditionStatus,on_delete=models.DO_NOTHING, null=True, blank=True)
    service = models.ForeignKey(Supplies,null=True, blank=True, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'ID: {self.id}, Unit: {self.unit}, Driver: {self.driver}, Supplier: {self.supplier}'

    
    '''def __str__(self):
        formatted_time = self.time_consult.strftime('%Y-%m-%d %H:%M:%S')
        unit_number = self.unit.truck_num if self.unit else 'N/A'
        return f'{formatted_time} - {self.status} - Unit {unit_number}'
    
    def save(self, *args, **kwargs):
        if not self.id:  # Solo si es un nuevo registro
            last_status = SupplieStatus.objects.filter(unit=self.unit).last()
            if last_status:
                if self.time_status:
                    self.time_dif = self.time_status - last_status.time_status
                    last_status.time_consult = self.time_status
                    last_status.save()
            else:
                self.time_dif = None

        super(SupplieStatus, self).save(*args, **kwargs)'''