from rest_framework import serializers

from app.serializers import RegionSerializer
from company.models import Company, Contact
from user.serializers import UserSerializer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    region_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Company
        fields = '__all__'
