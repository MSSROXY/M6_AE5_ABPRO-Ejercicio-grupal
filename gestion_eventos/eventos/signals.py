from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Evento

def crear_grupos_permisos(sender, **kwargs):
    admin_group, _ = Group.objects.get_or_create(name='Administradores')
    organizador_group, _ = Group.objects.get_or_create(name='Organizadores')
    asistente_group, _ = Group.objects.get_or_create(name='Asistentes')

    content_type = ContentType.objects.get_for_model(Evento)
    permisos = Permission.objects.filter(content_type=content_type)

    admin_group.permissions.set(permisos)
    organizador_group.permissions.set(permisos.filter(codename__in=['add_evento','change_evento']))
    asistente_group.permissions.clear()

class EventosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventos'

    def ready(self):
        post_migrate.connect(crear_grupos_permisos, sender=self)
