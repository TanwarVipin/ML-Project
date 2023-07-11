import sys
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from src import logger
from src import exception
import os
from dataclasses import dataclass
import logging
from src.utils import save_object
'''
 Modular Coding for the transformation of Data
'''
@dataclass
class data_transformation_config:
    preprocessor_path=os.path.join('artifact','preprocess.pkl')

class data_transformation:
    def __init__(self):
        self.data_transformation_config=data_transformation_config()
    def data_transformer_ob(self):
        try:
            num_feature=['reading score', 'writing score',]
            cat_feature=['gender', 'race/ethnicity', 'parental level of education', 'lunch',
                        'test preparation course']
            num_pipeline=Pipeline(
                steps=[
                    ('Imputer',SimpleImputer(strategy='median')),
                    ('Scaler',StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ('Imputer',SimpleImputer(strategy='most_frequent')),
                    ('OneHOTEncoder',OneHotEncoder())
                ]
            )
            logging.info('Data Transformation Is Completed')
            preprocessor=ColumnTransformer(
                [
                    ('Numerical',num_pipeline,num_feature),
                    ('Categorical',cat_pipeline,cat_feature)
                ]
            )
        except Exception as e:
            raise exception.CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info('READ Train and Test Completed')
            logging.info('Obtaining pre processor object')
            preprocessor_obj=self.data_transformer_ob()
            target='math_score'
            num_feature=['reading score','writing score']
            input_feature=train_df.drop(target,axis=1)

        except:
            pass
