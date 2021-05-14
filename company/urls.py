# Create your views here.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from company.views import CompanyViewSet
from user import views

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = (
    path('', include(router.urls)),
)
