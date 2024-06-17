from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import PredictSerializer
from rest_framework.permissions import AllowAny
from .models import Predict

# Create your views here.

class PredictListCreate(generics.ListCreateAPIView):
    def get_queryset(self):
        # user = self.request.user
        return Predict.objects.all()
    serializer_class = PredictSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
       if serializer.is_valid():
           serializer.save()
       else:
           print(serializer.errors)
           
           
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PredictSerializer
    permission_classes= [AllowAny]