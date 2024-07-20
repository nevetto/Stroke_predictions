# END TO END STROKE PREDICTION CLASSIFICATION PROJECT.

## Uderstanding the problem statement:
According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.
This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.

# STEPS....

Step #1:
. Create a folder
. Set up github repo
. Create an environment and activate it
    # conda create -p venv python==3.8 -y
. Push local github to global, create .gitignore then git pull in your folder.

Step #2:
. Create a template.py file to auto generate your folders and files.
. setup.py file and requirements.txt
. install requirements.txt using:
    # pip install -r requiirements.txt

step #3:
. create Src folder
. create __init__.py inside src folder
. create components folder inside src folder ad create the following files inside componets folder.
    .__init_.py inside components folder
        #The reason for adding __init__.py is for the folder to be seen as a package and can be used else where#
    . data_ingestion.py ( data ingestion is for reading data)
    . data_transfomation.py 
    . model_trainer.py 
    #All the files created inside components are for EDA purpose.#
. pipeline folder inside src folder, then create the following files inside pipeline folder
    . train_pipeline.py (for the training purpose)
    . predict_pipeline (for data predictions)

. Create exemption.py, logger.py and utils inside src folder.
. Create custom exemption in excemption.py
. create logger for execution, to log error and to trace error lines and execution that is taking place.

step #4:
Working on Dataset
## Dataset link: 
https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

## Attribute Information
1) id: unique identifier
2) gender: "Male", "Female" or "Other"
3) age: age of the patient
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6) ever_married: "No" or "Yes"
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8) Residence_type: "Rural" or "Urban"
9) avg_glucose_level: average glucose level in blood
10) bmi: body mass index ( a person's weight in kilograms (or pounds) divided by the square of height in meters (or feet))
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
12) stroke: 1 if the patient had a stroke or 0 if not



Performing EDA (explorative data analysis), model training and predictions

Working on model training

# Framework
react.js with JWT authentiation for the frontend and django for the backend.


# Observation:
I had imbalanced dataset and was solved with Resampling method

python 3.7 doesn't work with cors_origin, but python 3.8 works.

