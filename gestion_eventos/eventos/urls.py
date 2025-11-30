from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.ListaEventosView.as_view(), name='listar_eventos'),
    path('crear/', views.CrearEventoView.as_view(), name='crear_evento'),
    path('editar/<int:pk>/', views.EditarEventoView.as_view(), name='editar_evento'),
    path('eliminar/<int:pk>/', views.EliminarEventoView.as_view(), name='eliminar_evento'),
]
