from django.contrib import admin
from django.urls import path, include
from predictions.views import CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("predictions/user/register/", CreateUserView.as_view(), name="register"),
    path("predictions-auth/", include("rest_framework.urls")),
    path("predictions/", include("predictions.urls")),
]
