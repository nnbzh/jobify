# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import BasePermission

from company.models import Company
from company.serializers import CompanySerializer, ContactSerializer, InviteSerializer, RespondSerializer
from user.models import User
from utils.api_response import success_response, error_response
from utils.permissions import IsCompany, IsCompanyOwner


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

        if serializer.is_valid(raise_exception=True):
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

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, many=False)
        return success_response(data=serializer.data, message='', status=201)

    def get_permissions(self):
        return self.action_permissions[self.request.method]


@api_view(['POST'])
@permission_classes([IsCompanyOwner])
def create_contacts(request):
    response = Company.objects.add_contact(request.data.get('company_id'), request.data.get('value'))

    return success_response(response, '', 201)


@api_view(['POST'])
@permission_classes([IsCompanyOwner])
def invite(request):
    invited = User.objects.filter(id=request.data.get('user_id')).get()

    if invited.is_company:
        raise error_response('You cannot invite company', 400)

    serializer = InviteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return success_response(serializer.data, '')


@api_view(['POST'])
@permission_classes([IsCompanyOwner])
def respond(request):
    responded = User.objects.filter(id=request.data.get('user_id')).get()

    if not responded.is_company:
        raise error_response('You cannot respond to user', 400)

    serializer = RespondSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return success_response(serializer.data, '')
