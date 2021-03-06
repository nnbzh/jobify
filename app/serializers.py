from rest_framework import serializers

from app.models import Region


class RegionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=300)
    code = serializers.CharField(required=True, allow_blank=False, max_length=3)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance

    def create(self, validated_data):
        return Region.objects.create(**validated_data)
