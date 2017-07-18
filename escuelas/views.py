# coding: utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter
from rest_framework.filters import DjangoFilterBackend

import serializers
import models

"""
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000
"""

def home(request):
    return render(request, 'home.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = models.Escuela.objects.all()
    serializer_class = serializers.EscuelaSerializer

    def get_queryset(self):
        queryset = models.Escuela.objects.all()
        query = self.request.query_params.get('query', None)

        if query:
            filtro_cue = Q(cue__icontains=query)
            filtro_nombre = Q(nombre__icontains=query)

            queryset = queryset.filter(filtro_cue | filtro_nombre)

        return queryset

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = models.Contacto.objects.all()
    serializer_class = serializers.ContactoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    resource_name = 'eventos'
    queryset = models.Evento.objects.all()
    serializer_class = serializers.EventoSerializer

class RegionViewSet(viewsets.ModelViewSet):
    resource_name = 'regiones'
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
    #pagination_class = LargeResultsSetPagination

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = models.Perfil.objects.all()
    resource_name = 'perfiles'
    serializer_class = serializers.PerfilSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'apellido', "dni"]
    filter_fields = ['dni', 'cuit']

class MiPerfilViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        if not request.user.is_authenticated():
            return Response({'error': 'El usuario no esta autenticado.'})

        perfil = models.Perfil.objects.get(user=request.user)

        data = {
            'username': request.user.username,
            'nombre': perfil.nombre,
            'apellido': perfil.apellido,
            'permisosComoLista': perfil.obtenerListaDePermisos(),
            'permisos': perfil.obtenerPermisosComoDiccionario(),
            'grupos': perfil.obtenerListaDeGrupos(),
            'idPerfil': perfil.id
        }
        return Response(data)

class DistritoViewSet(viewsets.ModelViewSet):
    resource_name = 'distrito'
    queryset = models.Distrito.objects.all()
    serializer_class = serializers.DistritoSerializer
    #pagination_class = LargeResultsSetPagination

class LocalidadViewSet(viewsets.ModelViewSet):
    resource_name = 'localidad'
    queryset = models.Localidad.objects.all()
    serializer_class = serializers.LocalidadSerializer
    #pagination_class = LargeResultsSetPagination

class ProgramaViewSet(viewsets.ModelViewSet):
    resource_name = 'programa'
    queryset = models.Programa.objects.all()
    serializer_class = serializers.ProgramaSerializer

class TipoDeFinanciamientoViewSet(viewsets.ModelViewSet):
    queryset = models.TipoDeFinanciamiento.objects.all()
    serializer_class = serializers.TipoDeFinanciamientoSerializer

class TipoDeGestionViewSet(viewsets.ModelViewSet):
    resource_name = 'tipoDeGestion'
    queryset = models.TipoDeGestion.objects.all()
    serializer_class = serializers.TipoDeGestionSerializer

class AreaViewSet(viewsets.ModelViewSet):
    resource_name = 'area'
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer

class NivelViewSet(viewsets.ModelViewSet):
    resource_name = 'nivel'
    queryset = models.Nivel.objects.all()
    serializer_class = serializers.NivelSerializer

class ExperienciaViewSet(viewsets.ModelViewSet):
    resource_name = 'experiencia'
    queryset = models.Experiencia.objects.all()
    serializer_class = serializers.ExperienciaSerializer

class CargoViewSet(viewsets.ModelViewSet):
    resource_name = 'cargo'
    queryset = models.Cargo.objects.all()
    serializer_class = serializers.CargoSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    resource_name = 'contrato'
    queryset = models.Contrato.objects.all()
    serializer_class = serializers.ContratoSerializer

class PisoViewSet(viewsets.ModelViewSet):
    resource_name = 'piso'
    queryset = models.Piso.objects.all()
    serializer_class = serializers.PisoSerializer

class CargoEscolarViewSet(viewsets.ModelViewSet):
    resource_name = 'cargoEscolar'
    queryset = models.CargoEscolar.objects.all()
    serializer_class = serializers.CargoEscolarSerializer

class ComentarioTareaViewSet(viewsets.ModelViewSet):
    resource_name = 'comentarioTarea'
    queryset = models.ComentarioTarea.objects.all()
    serializer_class = serializers.ComentarioTareaSerializer

class MotivoTareaViewSet(viewsets.ModelViewSet):
    resource_name = 'motivoTarea'
    queryset = models.MotivoTarea.objects.all()
    serializer_class = serializers.MotivoTareaSerializer

class EstadoTareaViewSet(viewsets.ModelViewSet):
    resource_name = 'estadoTarea'
    queryset = models.EstadoTarea.objects.all()
    serializer_class = serializers.EstadoTareaSerializer

class PrioridadTareaViewSet(viewsets.ModelViewSet):
    resource_name = 'prioridadTarea'
    queryset = models.PrioridadTarea.objects.all()
    serializer_class = serializers.PrioridadTareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    resource_name = 'tarea'
    queryset = models.Tarea.objects.all()
    serializer_class = serializers.TareaSerializer
