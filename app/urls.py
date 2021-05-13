from django.urls import path
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()

urlpatterns = [
    path('regions', views.RegionApiView.as_view())
]
