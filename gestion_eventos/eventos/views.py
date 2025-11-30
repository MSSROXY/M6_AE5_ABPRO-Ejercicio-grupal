from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Evento
from .forms import EventoForm

# Vista de Home
def home(request):
    return render(request, 'eventos/home.html')

# Listar eventos
class ListaEventosView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'
    context_object_name = 'eventos'

# Crear evento
# Crear evento
class CrearEventoView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/crear_evento.html'
    permission_required = 'eventos.add_evento'
    title = "Crear Evento"  # <- aquí mismo

    def form_valid(self, form):
        form.instance.organizador = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para crear un evento.")
        return redirect('eventos:listar_eventos')


# Editar evento
class EditarEventoView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/editar_evento.html'
    permission_required = 'eventos.change_evento'
    title = "Editar Evento"  # <- aquí mismo

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para editar este evento.")
        return redirect('eventos:listar_eventos')

# Eliminar evento
class EliminarEventoView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Evento
    template_name = 'eventos/evento_confirm_delete.html'
    permission_required = 'eventos.delete_evento'
    success_url = reverse_lazy('eventos:listar_eventos')

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para eliminar este evento.")
        return redirect('eventos:listar_eventos')
