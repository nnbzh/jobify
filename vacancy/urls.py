# Create your views here.
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vacancy import views

router = DefaultRouter()
router.register(r'business-types', views.BusinessTypeViewSet, basename='business-types')
router.register(r'experience-types', views.ExperienceTypeViewSet, basename='experience-types')
router.register(r'vacancies', views.VacancyViewSet, basename='vacancies')

urlpatterns = [
    path('api/', include(router.urls)),
]
