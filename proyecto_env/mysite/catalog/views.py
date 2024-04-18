from django.shortcuts import render
from .models import Jugadora,InstanciaJugadora
from django.shortcuts import render, redirect

def index(request):
    """
       Función vista para la página inicio del sitio.
       """
    # Genera contadores de algunos de los objetos principales
    num_jugadoras=Jugadora.objects.all().count
    num_instancia=InstanciaJugadora.objects.all().count

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,'index.html', context={'num_jugadoras':num_jugadoras,'num_instacia':num_instancia})

def jugadoras(request):
    jugadoras_list=Jugadora.objects.all()
    return render(request, 'jugadoras.html', {'jugadoras_list': jugadoras_list})

def detalle_jugadora(request, jugadora_id):
    jugadora = get_object_or_404(Jugadora, pk=jugadora_id)
    return render(request, 'detalle_jugadora.html', {'jugadora': jugadora})