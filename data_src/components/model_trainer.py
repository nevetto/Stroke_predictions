import os
import sys
from dataclasses import dataclass

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from catboost import CatBoostClassifier
from xgboost import XGBClassifier

from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np

from sklearn.metrics import accuracy_score

import warnings

from data_src.exception import CustomException
from data_src.logger import logging

from data_src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Logistic Regression": LogisticRegression(),
                "K-Neighbors Classifier": KNeighborsClassifier(),
                "Decision Tree": tree.DecisionTreeClassifier(),
                "Random Forest Classifier": RandomForestClassifier(),
                "XGBClassifier": XGBClassifier(),
                "CatBoosting Classifier": CatBoostClassifier(verbose=False),
                "AdaBoost Classifier": AdaBoostClassifier()
            }
            # number of trees in random forest
            n_estimators = [int(x) for x in np.linspace(start = 18, stop=80, num=10)]
            # number of feartures to consider at every split
            max_features = ['auto', 'sqrt']
            # maximum number of levels
            max_depth = [2,4]
            # minimum number of samples required to spit the node
            min_samples_split =[2,5]
            # minimum number of samples required at each leaf node
            min_samples_leaf = [1,2]
            # method for selecting samples to train each tree
            bootstrap =[True, False]
            
            params={
                "Decision Tree": {
                    'criterion':['gini', 'entropy'],
                     
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                
                "K-Neighbors Classifier":{},
                
                "Random Forest Classifier":{
                    'n_estimators': n_estimators,
                    'max_features': max_features,
                    'max_depth': max_depth,
                    'min_samples_split': min_samples_split,
                    'min_samples_leaf': min_samples_leaf,
                    'bootstrap': bootstrap
                    },               
                "Logistic Regression":{},
                "XGBoost":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "XGBClassifier":{},
                
                "CatBoosting Classifier":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Classifier":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                              models=models,param=params)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            print(best_model)

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            
            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            accuracy = accuracy_score(y_test, predicted)
            # score = r2_score(y_test, predicted)*100
            # print(" Accuracy of the model is %.2f" %score)
            return r2_square , accuracy

           
            



            
        except Exception as e:
            raise CustomException(e,sys)