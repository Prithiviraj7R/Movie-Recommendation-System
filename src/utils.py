import os
import sys
import re
import dill

from src.exception import CustomException
from src.model.model import DeepAutoEncoder
from src.model.utils import loss_function

from keras.optimizers import SGD

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
    
def evaluate_model(model_file_path,embeddings_file_path,train_data,test_data):

    try:
        input_shape = train_data.shape[1]
        layers = [256,256,512,256,256]
        activation = 'selu'
        output_activation = 'selu'
        dropout = 0.8
        regularization_encoder = regularization_decoder = 0.001

        model_definition = DeepAutoEncoder(input_shape,layers,activation,output_activation,dropout,regularization_encoder,regularization_decoder)
        model = model_definition.get_model()

        model.compile(optimizer=SGD(learning_rate=0.001,momentum=0.9),loss=loss_function)

        model.fit(x=train_data,y=train_data,epochs=1000,batch_size=64,validation_split=0.2)

        y_pred = model.predict(test_data)
        loss = loss_function(test_data,y_pred)

        encoder_model = model_definition.get_encoder_model()

        save_file(model_file_path,encoder_model)

        return loss
        
    except Exception as e:
        raise CustomException(e,sys)




