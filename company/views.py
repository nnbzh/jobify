# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import BasePermission

from company.models import Company, Contact
from company.serializers import CompanySerializer, ContactSerializer
from utils.api_response import success_response, error_response
from utils.permissions import IsCompany


class CompanyListAPIView(ListCreateAPIView):
    action_permissions = {
        'GET': [BasePermission()],
        'POST': [IsCompany()]
    }
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        obj = dict(request.data)
        obj['user_id'] = request.user.id
        serializer = self.get_serializer(data=obj)
        if serializer.is_valid():
            serializer.save()
        return success_response(data=serializer.data, message='', status=200)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data, message='', status=200)

    def get_permissions(self):
        return self.action_permissions[self.request.method]


class CompanyDetailsApiView(RetrieveUpdateAPIView):
    action_permissions = {
        'GET': [BasePermission()],
        'PUT': [IsCompany()]
    }
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        return self.action_permissions[self.request.method]


@api_view(['POST'])
@permission_classes([IsCompany])
def create_contacts(request, pk):
    company = request.user.company.get()

    if pk != company.id:
        return error_response("That's not your company", 400)

    obj = dict(request.data)
    obj['company_id'] = pk
    serializer = ContactSerializer(data=obj)

    if serializer.is_valid():
        serializer.save()

    Company.objects.filter(id=pk).update(contact_id=serializer.data.get('id'))

    return success_response(serializer.data, '')
