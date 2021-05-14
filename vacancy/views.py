from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.permissions import BasePermission

import vacancy.serializers as serializers
import vacancy.models as models
from utils.permissions import IsCompany


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class CreateListRetrieveViewSet(mixins.RetrieveModelMixin, CreateListViewSet):
    pass


class ExperienceTypeViewSet(CreateListViewSet):
    queryset = models.ExperienceType.objects.all()
    serializer_class = serializers.ExperienceTypeSerializer


class BusinessTypeViewSet(CreateListViewSet):
    queryset = models.BusinessType.objects.all()
    serializer_class = serializers.BusinessTypeSerializer


class VacancyViewSet(CreateListRetrieveViewSet):
    action_permissions = {
        'GET': [BasePermission()],
        'POST': [IsCompany()]
    }
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer

    def get_permissions(self):
        return self.action_permissions[self.request.method]
