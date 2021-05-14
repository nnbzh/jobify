from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer
from utils.api_response import success_response, error_response
from .serializers import UserAvatarSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.data['is_company']:
            User.objects.create_company(serializer.data['email'], serializer.data['password'])
        else:
            User.objects.create_user(serializer.data['email'], serializer.data['password'])
        return success_response(data=serializer.data, message="User created", status=201)
    else:
        return error_response(message=serializer.errors, status=400)


class UserAvatarUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserAvatarSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data, '')
        else:
            return error_response(serializer.errors, 400)
