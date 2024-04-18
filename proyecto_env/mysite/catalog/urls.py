from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('jugadoras/', views.jugadoras, name='jugadoras_list'),
    path('jugadoras/<int:jugadora_id>/', views.detalle_jugadora, name='detalle_jugadora'),
]