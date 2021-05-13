from rest_framework import serializers

from app.serializers import RegionSerializer
from company.models import Company, ContactType, Contact


class CompanySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    contact_type = ContactTypeSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
