from celery import shared_task
from datetime import datetime

@shared_task
def my_scheduled_task():
    try:
        # Cuerpo de la tarea
        print(f"Tarea programada ejecutada en {datetime.now()}")
        # ... tu lógica aquí ...
    except Exception as e:
        # Registrar cualquier excepción
        print(f"Error en la tarea: {e}")
        raise  # Vuelve a levantar la excepción para que Celery lo detecte como un fallo
