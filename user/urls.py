# Create your views here.
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from user import views

urlpatterns = (
    path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', views.register),
    path('image/upload', views.UserAvatarUpload.as_view()),
)
