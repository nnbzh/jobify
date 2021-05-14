# Create your views here.
from django.conf.urls.static import static
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from jobify import settings
from user import views

urlpatterns = (
    path('login', obtain_jwt_token),
    path('register', views.register),
    path('image/upload', views.UserAvatarUpload.as_view()),
)
