import django_tables2 as tables
from supplies.models import SupplieStatus

class SupplieTable(tables.Table):
    time_dif = tables.Column(verbose_name='Tiempo en estatus', empty_values=(), orderable=False)

    class Meta:
        model = SupplieStatus
        fields = ('time_status','time_consult','time_dif', 'status', 'unit', 'driver', 'turn', 'supplier', 'condition')  # Define los campos a mostrar
        order_by = '-time_status'
        attrs = {
            'class': 'custom-table'
        }
        
    time_status = tables.DateTimeColumn(format='d-m-Y H:i:s', verbose_name='Fecha y Hora inicio',orderable=True)
    time_consult = tables.DateTimeColumn(format='d-m-Y H:i:s', verbose_name='Fecha y Hora Fin',orderable=False)
    status = tables.Column(verbose_name='Estatus',orderable=False)
    unit = tables.Column(verbose_name='Unidad',orderable=False)
    driver = tables.Column(verbose_name='Operador',orderable=False)
    turn = tables.Column(verbose_name='Turno',orderable=False)
    supplier = tables.Column(verbose_name='Proveedor',orderable=False)
    condition = tables.Column(verbose_name='Información Adicional',orderable=False)
    
    def render_time_dif(self, value, record):
        if record.time_dif:
            hours, remainder = divmod(record.time_dif.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            return f'{int(hours)}h {int(minutes)}m {int(seconds)}s'
        return '-'
    
    