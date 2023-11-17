from django.db import models

class DeviceData(models.Model):
    asset_id = models.IntegerField()
    engine_model = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    number_plates = models.CharField(max_length=100)
    altitude = models.FloatField()
    date = models.DateTimeField()
    gps_distance = models.FloatField()
    gps_speed = models.FloatField()
    ignition = models.BooleanField()
    is_satellite_source = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    nearest_city_name = models.CharField(max_length=100)
    nearest_city_distance = models.FloatField()
    nearest_city_orientation = models.CharField(max_length=100)
    nearest_city_reference = models.CharField(max_length=100)
    orientation = models.FloatField()
    orientation_label = models.CharField(max_length=100)
    satellites = models.IntegerField()
    serial_number = models.CharField(max_length=100)
    sim_imei = models.CharField(max_length=100)
    vehicle_brand = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=100)
    vehicle_year = models.CharField(max_length=100)
    vin = models.CharField(max_length=100)

    def __str__(self):
        return f"DeviceData: {self.asset_id}"

class Event(models.Model):
    device = models.ForeignKey(DeviceData, on_delete=models.CASCADE)
    event_type = models.IntegerField()
    event = models.CharField(max_length=100)
    event_description = models.CharField(max_length=100)
    event_type_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Event: {self.event}"