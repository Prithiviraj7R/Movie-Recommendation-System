'''
AutoEncoder model is then used to train the model and
tested on the validation set to evaluate the 
model performance. Model is then used to calculate movie 
embeddings and stored for later use.
'''

import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import evaluate_model

@dataclass
class ModelTrainerConfig:
    model_path: str = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_data,test_data):
        logging.info("Model Training has started!")
        try:
            latent_size_list = [1000,500,300,200,100]
            model_report = {}
            for latent_size in latent_size_list:
                model_report[str(latent_size)] = evaluate_model(train_data,test_data,latent_size)

            ## choose the best latent_size and the model

            
            pass
        except Exception as e:
            raise CustomException(e,sys)