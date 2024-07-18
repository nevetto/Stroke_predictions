from django.db import models
from django.contrib.auth.models import User
import dill
import pickle
 
# from cufflinks.ta import dmi
from sklearn.preprocessing import OneHotEncoder
from django.contrib.auth.models import User
import os 

import sys
 

class Predict(models.Model):        
     
    Male =models.CharField(max_length=20, blank=True, null=True)
    Female =models.CharField(max_length=20, blank=True, null=True)
    ever_married =models.CharField(max_length=30,blank=True, null=True)
    Not_married =models.CharField(max_length=30,blank=True, null=True)
    Govt_job =models.CharField(max_length=30,blank=True, null=True)
    Private =models.CharField(max_length=30,blank=True, null=True)
    Self_employed =models.CharField(max_length=30,blank=True, null=True)
    children =models.CharField(max_length=30,blank=True, null=True)
    Rural =models.CharField(max_length=30,blank=True, null=True)
    Urban =models.CharField(max_length=30,blank=True, null=True)
    Unknown_smoke =models.CharField(max_length=30,blank=True)
    formerly_smoked =models.CharField(max_length=30,blank=True)    
    never_smoked =models.CharField(max_length=30,blank=True)    
    smokes =models.CharField(max_length=30,blank=True)
    
    
    age = models.FloatField(max_length=20, blank=True)
    hypertension = models.IntegerField(blank=True)
    heart_disease = models.IntegerField(blank=True)
    avg_glucose_level = models.FloatField(blank=True)
    bmi = models.FloatField(blank=True)
     
    
    result = models.FloatField(max_length=100,blank=True)
    
    
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="predict")
     
    
    def save(self, *args, **kwargs):  
        
        enc = OneHotEncoder(handle_unknown = "ignore")  
     
              
        model_path1=os.path.join("model.pkl")        
        model_path=open(model_path1, "rb")
        model=dill.load(model_path) 
        
         
        # with open("predictions\encoder.pickle", 'rb') as ohe:                     
        #     enc = pickle.load(ohe)
            
            # enc = OneHotEncoder()
            
            
        
        # preprocessor_path = os.path.join("proprocessor.pkl")  
        # preprocessor_path1 = open(preprocessor_path, "rb")
        # preprocessor=dill.load(preprocessor_path1)
        
        # ohe = OneHotEncoder()
        
        enc_ode= enc.fit_transform([[self.Male, self.Female, self.ever_married,self.Not_married, self.Govt_job, self.Private, self.Self_employed, self.children, self.Rural,
                                                   self.Urban, self.Unknown_smoke,self.formerly_smoked,
                                                   self.never_smoked,self.smokes, self.age,self.hypertension,self.heart_disease,self.avg_glucose_level, self.bmi]])
        
        self.result= model.predict( enc_ode)
        
       
         
        
        return super().save(*args, **kwargs)

    # class Meta:
    #     ordering = ['-date']
        
    def __str__(self):
        return self.Male
