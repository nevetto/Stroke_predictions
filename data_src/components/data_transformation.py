import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from imblearn.over_sampling import (RandomOverSampler)

from data_src.exception import CustomException
from data_src.logger import logging
import os

from data_src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        
        '''
        try:
            self.numerical_columns = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi']
            self.categorical_columns = ['gender', 'ever_married', 'work_type', 'Residence_type','smoking_status',]
            
            num_pipeline= Pipeline(
                steps=[
                # ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("one_hot_encoder",OneHotEncoder(handle_unknown = "ignore")),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {self.categorical_columns}")
            logging.info(f"Numerical columns: {self.numerical_columns}")
            
          

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,self.numerical_columns),
                ("cat_pipelines",cat_pipeline,self.categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            
            

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()
            
             
            target_column_name="stroke"
            id_column = 'id'
            unknown = 'Unnamed: 0'
            self.numerical_columns=['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi']

            input_feature_train_df=train_df.drop(columns=([target_column_name, id_column, unknown]),axis=1)
            target_feature_train_df=train_df[target_column_name]
                  
                

            input_feature_test_df=test_df.drop(columns=([target_column_name, id_column]),axis=1)
            target_feature_test_df=test_df[target_column_name]  
            print(input_feature_test_df) 
            
            
            
 
            
            resamp = RandomOverSampler()
            input_feature_train_df, target_feature_train_df = resamp.fit_resample(input_feature_train_df,target_feature_train_df )
            input_feature_test_df, target_feature_test_df = resamp.fit_resample( input_feature_test_df,target_feature_test_df)
            
            count_X1 = target_feature_train_df.value_counts()
            print('this are the values for   balanced data', count_X1)
            count_X2 = input_feature_train_df.value_counts()
            print('this are the values for   balanced data', count_X2)
            
            logging.info( f"imbalanced dataset has been resolved")
            
             
            
            
            
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df) 
           
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
           
            
            

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
