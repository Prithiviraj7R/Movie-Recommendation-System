import os
import sys
import re
import dill

from src.exception import CustomException

def extract_movie_name(title):
    try:
        match = re.match(r'^(.*?)\s*\(\d{4}\)?$', title)
        return match.group(1) if match else title
    except Exception as e:
        CustomException(e,sys)

def save_file(file_path,file):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(file, file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(latent_size,train_data,test_data):
    pass
