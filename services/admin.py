from django.contrib import admin
from .models import Trips, Address, Driver, Origin, Month, ServiceType, Supplier, Truck, Trailer,IdConcept,MonthExpenses,Route,RoutePoint
from supplies.models import Supplies, Turn, Status, PortSupplier, SupplieStatus, ConditionStatus,WeekDays,TypeSupplie
from backtasks.models import DeviceData,Event
# Register your models here.
admin.site.register(Trips)
admin.site.register(Address)
admin.site.register(Driver)
admin.site.register(Origin)
admin.site.register(Month)
admin.site.register(ServiceType)
admin.site.register(Supplier)
admin.site.register(Truck)
admin.site.register(Trailer)
admin.site.register(Supplies)
admin.site.register(Turn)
admin.site.register(Status)
admin.site.register(PortSupplier)
admin.site.register(SupplieStatus)
admin.site.register(ConditionStatus)
admin.site.register(WeekDays)
admin.site.register(TypeSupplie)
admin.site.register(IdConcept)
admin.site.register(MonthExpenses)
admin.site.register(Route)
admin.site.register(RoutePoint)
admin.site.register(DeviceData)
admin.site.register(Event)

