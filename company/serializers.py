from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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
    user_id = serializers.IntegerField(write_only=True, validators=[
        UniqueValidator(
            queryset=Company.objects.all(),
            message="User already have a company"
        )
    ], required=False)
    create_date = serializers.DateTimeField(input_formats=['%Y-%m-%d'])
    bin = serializers.IntegerField(validators=[
        UniqueValidator(
            queryset=Company.objects.all(),
            message="Company with this BIN is already exists"
        )
    ])

    class Meta:
        model = Company
        fields = '__all__'
