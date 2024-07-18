from django.contrib import admin
from django.urls import path, include
from predictions.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("predictions/user/register/", CreateUserView.as_view(), name="register"),
    path("predictions/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("predictions/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("predictions-auth/", include("rest_framework.urls")),
    path("predictions/", include("predictions.urls")),
]
