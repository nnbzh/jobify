from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)
    is_company = serializers.BooleanField(default=False)
    password = serializers.CharField(max_length=50, write_only=True)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('name', instance.name)
        instance.first_name = validated_data.get('first_name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.name)
        instance.save()
        return instance

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UserAvatarSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["avatar"]

    def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(**kwargs)
