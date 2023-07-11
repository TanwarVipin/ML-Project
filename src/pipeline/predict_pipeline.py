import sys
import pandas as pd
import numpy as np
import random
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self) -> None:
        pass
        
class CustomData():
    def __init__(self,gender,lunch:int,reading_score:int,race_ethincity:str) -> None:
        self.gender=gender
        self.lunch=lunch
        self.reading_Score=reading_score
        self.race=race_ethincity



