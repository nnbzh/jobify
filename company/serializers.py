from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.serializers import RegionSerializer
from company.models import Company, Contact, Invite
from user.serializers import UserSerializer


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


class ContactSerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'


class InviteSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    user = UserSerializer(read_only=True)

    company_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Invite
        fields = '__all__'
