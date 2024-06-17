from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Predict

class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predict
        fields = ['first_name', 'second_name','Male', 'Female', 'ever_married','Not_married','Govt_job', 'Private', 'Self_employed', 'children',  'Rural', 'Urban', 'Unknown_smoke','formerly_smoked', 'never_smoked','smokes', 'age', 'hypertension', 'heart_disease', 'avg_glucose_level','bmi', 'result', 'date']
        # extra_kwargs = {"author": {"read_only": False}}