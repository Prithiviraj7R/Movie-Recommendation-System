'''
Read the required data and store it in artifacts.
This will be accessed during data transformation.
'''

import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_extraction import DataExtraction,DataExtractionConfig
from src.components.model_training import ModelTrainer,ModelTrainerConfig

import pandas as pd

@dataclass
class DataIngestionConfig:
    movies_data_path: str = os.path.join('artifacts','movies.csv')
    ratings_data_path: str = os.path.join('artifacts','ratings.csv')
    links_data_path: str = os.path.join('artifacts','links.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion has been initiated")
        try:
            movies_df = pd.read_csv(r'notebook\data\ml-25m\movies.csv')
            ratings_df = pd.read_csv(r'notebook\data\ml-25m\ratings.csv')
            links_df = pd.read_csv(r'notebook\data\ml-25m\links.csv')

            logging.info("Data has been read into a dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion_config.movies_data_path),exist_ok=True)

            movies_df.to_csv(self.data_ingestion_config.movies_data_path, index=False, header=True)
            ratings_df.to_csv(self.data_ingestion_config.ratings_data_path, index=False, header=True)
            links_df.to_csv(self.data_ingestion_config.links_data_path, index=False, header=True)

            logging.info("Data Ingestion Complete")

            return(
                self.data_ingestion_config.movies_data_path,
                self.data_ingestion_config.ratings_data_path,
                self.data_ingestion_config.links_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    movies_path,ratings_path,_ = obj.initiate_data_ingestion()

    data_extraction = DataExtraction()
    train_data,test_data,_,_,_ = data_extraction.initiate_data_extraction(movies_path,ratings_path)

    model_trainer = ModelTrainer()
    report = model_trainer.initiate_model_training(train_data,test_data)
    print(report)

