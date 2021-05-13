from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)
    first_name = serializers.CharField(max_length=300)
    last_name = serializers.CharField(max_length=300)
    is_staff = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('name', instance.name)
        instance.first_name = validated_data.get('first_name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.name)
        instance.is_staff = validated_data.get('is_staff')
        instance.save()
        return instance

    def create(self, validated_data):
        return User.objects.create(**validated_data)
