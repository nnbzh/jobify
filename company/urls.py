# Create your views here.
from django.urls import path

# router = DefaultRouter()
# router.register(r'companies', CompanyViewSet, basename='company')
from company import views

# from company.views import CompanyViewSet

urlpatterns = [
    path(r'companies', views.CompanyListAPIView.as_view()),
    path(r'companies/<int:pk>', views.CompanyDetailsApiView.as_view()),
    path(r'companies/contacts', views.create_contacts),
    path(r'companies/invite', views.invite),
    path(r'companies/respond', views.respond),
]
