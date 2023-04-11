from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Incidencia


def index(request):
    return HttpResponse("Hello, world")

def formulario(request):
    datos = Incidencia.objects.filter(remove=False)
    return render(request, 'formulario.html', {'datos': datos})

@csrf_exempt
def guardar_incidencia(request):
    if request.method == 'POST' :
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        prioridad = request.POST.get('Prioridad')
        incidencia = Incidencia.objects.create(titulo=titulo, descripcion=descripcion, prioridad=prioridad, remove=False)
        if incidencia:
            return JsonResponse({'status': 'ok',
                             'id': incidencia.id}
                            )
        else:
            return JsonResponse({'status': 'error'})    
    else:
        return JsonResponse({'status': 'error'})
    
def obtener_incidencias(request):
    incidencias = Incidencia.objects.filter(remove=False)
    data = list(incidencias.values())
    print(data)
    return JsonResponse(data, safe=False) 

@csrf_exempt
def eliminar_incidencia(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        incidencia = Incidencia.objects.get(id=id)
        if incidencia:
            incidencia.remove = True
            incidencia.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'})
    else:
        return JsonResponse({'status': 'error'})

@csrf_exempt
def editar_incidencia(request):
    if request.method == 'POST' :
        id = request.POST.get('id')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        prioridad = request.POST.get('Prioridad')
        incidencia = Incidencia.objects.get(id=id)
        if incidencia:
            incidencia.titulo = titulo
            incidencia.descripcion = descripcion
            incidencia.prioridad = prioridad
            incidencia.save()
            return JsonResponse({'status': 'ok',
                                'id': incidencia.id}
                                )
        else:
            return JsonResponse({'status': 'error'})
    else:
        return JsonResponse({'status': 'error'})