from django.contrib.auth import authenticate
from django.http import JsonResponse

# Create your views here.
def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse({'mensaje': 'Autenticado exitosamente'})
        else:
            return JsonResponse({'mensaje': 'Credenciales inválidas'}, status=401)

    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)