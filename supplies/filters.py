import django_filters
from .models import SupplieStatus

class SupplieFilter(django_filters.FilterSet):
    class Meta:
        model = SupplieStatus
        fields = ('status', 'unit', 'driver', 'turn', 'supplier','condition' )  # campos a filtrar
