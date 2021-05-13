from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from app.models import Region
from app.serializers import RegionSerializer


class RegionApiView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
