import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import data_transformation

@dataclass          #directly define class variable without using init
class data_ingestion_config():
    train_data_path: str=os.path.join('artifact','train.csv')
    test_data_path: str=os.path.join('artifact','test.csv')
    raw_data_path: str=os.path.join('artifact','data.csv')
    
class data_ingestion():
    def __init__(self):
        self.ingesttion_config=data_ingestion_config()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method')
        try:
            df=pd.read_csv('C:/Users/priya/ml_projects/notebooks/data/stud.csv')

            logging.info('Read the dataset as DataFrame')
        
            os.makedirs(os.path.dirname(self.ingesttion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingesttion_config.raw_data_path,index=False,header=True)

            logging.info('Train test split initiate')

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingesttion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingesttion_config.test_data_path,index=False,header=True)
            
            logging.info('Ingestion Completed')

            return(
                self.ingesttion_config.train_data_path,
                self.ingesttion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    obj=data_ingestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=data_transformation()
    data_transformation.initiate_data_transormation(train_data,test_data)