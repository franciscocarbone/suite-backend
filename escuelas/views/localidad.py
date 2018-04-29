# coding: utf-8
from __future__ import unicode_literals
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from escuelas import models, serializers


class LocalidadViewSet(viewsets.ModelViewSet):
    resource_name = 'localidad'

    queryset = models.Localidad.objects.all()
    serializer_class = serializers.LocalidadSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre']
    filter_fields = ['nombre', 'distrito']