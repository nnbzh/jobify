from rest_framework import serializers
from company.serializers import CompanySerializer
from vacancy.models import ExperienceType, BusinessType, Vacancy, Requirement, Responsibility, Condition


class ExperienceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceType
        fields = '__all__'


class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)
    experience_type_id = serializers.IntegerField(write_only=True)
    business_type_id = serializers.IntegerField(write_only=True)

    company = CompanySerializer(read_only=True)
    experience_type = ExperienceTypeSerializer(read_only=True)
    business_type = BusinessTypeSerializer(read_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'experience_type_id', 'experience_type',
                  'business_type_id', 'business_type', 'company_id', 'company',)


class ResponsibilitySerializer(serializers.ModelSerializer):
    vacancy_id = serializers.IntegerField(write_only=True)
    vacancy = VacancySerializer(read_only=True)

    class Meta:
        model = Responsibility
        fields = '__all__'


class RequirementSerializer(serializers.ModelSerializer):
    vacancy_id = serializers.IntegerField(write_only=True)
    vacancy = VacancySerializer(read_only=True)

    class Meta:
        model = Requirement
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    vacancy_id = serializers.IntegerField(write_only=True)
    vacancy = VacancySerializer(read_only=True)

    class Meta:
        model = Condition
        fields = '__all__'
