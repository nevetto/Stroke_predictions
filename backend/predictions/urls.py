from django.urls import path
from . import views

urlpatterns = [
    path("predict/", views.PredictListCreate.as_view(), name="predict_list"),
    path("predict/delete/<int:pk>/", views.PredictDelete.as_view(), name="delete-predict"),
]
