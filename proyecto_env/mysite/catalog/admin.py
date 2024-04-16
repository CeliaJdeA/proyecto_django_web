from django.contrib import admin
from .models import ( Jugadora, Categoria, Nacionalidade,Posicione, InstanciaJugadora)

#admin.site.register(Jugadora)
admin.site.register(Categoria)
admin.site.register(Nacionalidade)
admin.site.register(Posicione)

@admin.register(Jugadora)
class JugadoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos','dorsal','posicion')
    fields = [('nombre','apellidos','dorsal'), 'posicion', 'nacionalidad', 'categoria']

@admin.register(InstanciaJugadora)
class InstanciaJugadoraAdmin(admin.ModelAdmin):
    list_display = ('jugadora','id')
