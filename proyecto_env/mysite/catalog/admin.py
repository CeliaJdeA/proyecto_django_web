from django.contrib import admin
from .models import ( Jugadora, Categoria, Nacionalidade,Posicione)

admin.site.register(Jugadora)
admin.site.register(Categoria)
admin.site.register(Nacionalidade)
admin.site.register(Posicione)