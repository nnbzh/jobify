# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.permissions import BasePermission

import vacancy.models as models
import vacancy.serializers as serializers
from utils.api_response import success_response
from utils.permissions import IsCompanyOwner


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data, message='', status=200)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return success_response(data=serializer.data, message='', status=201)


class CreateListRetrieveViewSet(mixins.RetrieveModelMixin, CreateListViewSet):
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data, message='', status=200)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return success_response(data=serializer.data, message='', status=201)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, many=False)
        return success_response(data=serializer.data, message='', status=201)


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return success_response(data=serializer.data, message='', status=201)


class ExperienceTypeViewSet(CreateListViewSet):
    queryset = models.ExperienceType.objects.all()
    serializer_class = serializers.ExperienceTypeSerializer


class BusinessTypeViewSet(CreateListViewSet):
    queryset = models.BusinessType.objects.all()
    serializer_class = serializers.BusinessTypeSerializer


class VacancyViewSet(CreateListRetrieveViewSet):
    action_permissions = {
        'GET': [BasePermission()],
        'POST': [IsCompanyOwner()]
    }
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer

    def get_permissions(self):
        return self.action_permissions[self.request.method]


class ResponsibilityViewSet(CreateViewSet):
    permission_classes = (IsCompanyOwner,)
    queryset = models.Responsibility.objects.all()
    serializer_class = serializers.ResponsibilitySerializer


class ConditionViewSet(CreateViewSet):
    permission_classes = (IsCompanyOwner,)
    queryset = models.Condition.objects.all()
    serializer_class = serializers.ConditionSerializer


class RequirementViewSet(CreateViewSet):
    permission_classes = (IsCompanyOwner,)
    queryset = models.Requirement.objects.all()
    serializer_class = serializers.RequirementSerializer
