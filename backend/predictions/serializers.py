from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Predict

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
    
class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predict
        fields = ['id','Male', 'Female', 'ever_married','Not_married','Govt_job', 'Private', 'Self_employed', 'children',  'Rural', 'Urban', 'Unknown_smoke','formerly_smoked', 'never_smoked','smokes', 'age', 'hypertension', 'heart_disease', 'avg_glucose_level','bmi', 'result', 'date', 'author']
        extra_kwargs = {"author": {"read_only": True}}
