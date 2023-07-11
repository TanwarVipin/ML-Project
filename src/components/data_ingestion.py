import os
import sys
from src import exception
from src import logger
import logging

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from dataclasses import dataclass   #use to create class variable

@dataclass
class data_ingestion_config:
    train_path: str=os.path.join('artifacts','train.csv')
    test_path: str=os.path.join('artifacts','test.csv')
    raw_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=data_ingestion_config()
    def initiate_data_ingestion(self):
        logging.info('Enter The Data Ingestion Component')
        try:
            df=pd.read_csv(r'D:\Project\src\notebook\data\data.csv')
            logging.info('Exported Raw Data')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_path))
            df.to_csv(self.ingestion_config.raw_path,index=False,header=True)
            logging.info('Train Test Split')
            train,test=train_test_split(df,test_size=0.3,random_state=42)
            train.to_csv(self.ingestion_config.train_path,index=False,header=True)
            test.to_csv(self.ingestion_config.test_path,index=False,header=True)
            logging.info('Data Ingestion Completed')
            return self.ingestion_config.train_path,self.ingestion_config.test_path
        except Exception as e:
            raise exception.CustomException(e,sys)
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()

        

        




