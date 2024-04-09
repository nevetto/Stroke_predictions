import sys
from cufflinks.ta import dmi
import pandas as pd
from data_src.exception import CustomException
from data_src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        
    #     ['Unnamed: 0', 'age', 'hypertension', 'heart_disease',
    #    'avg_glucose_level', 'bmi', 'Unnamed: 0.1', 'id'],
    #   dtype='object') ............ Index(['gender', 'ever_married', 'work_type', 'c',
    #    'smoking_status']
    
    class CustomData:
        def __init__(self, 
                     age: float, 
                     hypertension: int, 
                     heart_disease: int, 
                     avg_glucose_level: float, 
                     bmi: float, 
                     gender:str, 
                     ever_married:str, 
                     work_type: str, 
                     Residence_type: str):
            self.age=age
             
            self.hypertension= hypertension
            
            self.heart_disease = heart_disease 
            self.avg_glucose_level = avg_glucose_level
            self.bmi =bmi
            self.gender = gender
            self.ever_married = ever_married
            self.work_type = work_type
            self.Residence_type = Residence_type
            
        def get_data_as_data_frame(self):
            try:
                custom_data_input_dict = {
                    "gender": [self.age],              
                    "hypertension": [self.hypertension],                    
                    "heart_disease ": [self.heart_disease],
                    "avg_glucose_level": [self.avg_glucose_level], 
                    "bmi": [self.bmi],
                    "gender" :[self.gender ],
                    "ever_married": [self.ever_married],
                    "work_type": [self.work_type],
                    "Residence_type": [self.Residence_type],
                }
                
                return pd.DataFrame(custom_data_input_dict)
            except Exception as e:
                raise CustomException(e, sys)
             
    