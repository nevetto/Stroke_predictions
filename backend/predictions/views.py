from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PredictSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Predict

# Create your views here.

class PredictListCreate(generics.ListCreateAPIView):
    serializer_class = PredictSerializer
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Predict.objects.filter(author=user)
        # return Predict.objects.all()
    
    
    def perform_create(self, serializer):
        if serializer.is_valid():
           serializer.save(author=self.request.user)
        else:
           print(serializer.errors)
           
           
class PredictDelete(generics.DestroyAPIView):
    serializer_class = PredictSerializer
    permission_classes = [IsAuthenticated]    

    def get_queryset(self):
        user = self.request.user
        return Predict.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes= [AllowAny]