# END TO END STROKE PREDICTION CLASSIFICATION PROJECT.

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
        #The reason of adding __init__.py is because the folder will be seen as package and can be used else where#
    . data_ingestion.py ( data ingestion is reading data from)
    . data_transfomation.py 
    . model_trainer.py 
    #All the files created inside componets are for EDA purpose.#
. pipeline folder inside src folder, then create the following files inside pipeline folder
    . train_pipeline.py (for the training purpose)
    . predict_pipeline (for sata predictions)

. Create exempton.py, logger.py and utils inside src folder.
. Create custom exemption in excemption.py
. create logger for execution, to log error and to trace error lines and execution that is taking place.

