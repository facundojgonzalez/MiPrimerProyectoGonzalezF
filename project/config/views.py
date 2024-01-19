from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola!")

def saludo2(request):
    nombre = input('Ingresa tu nombre')
    return HttpResponse(f'Tu nombre es {nombre}')