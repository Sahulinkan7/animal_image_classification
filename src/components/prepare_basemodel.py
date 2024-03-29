from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import PrepareBaseModelConfig
from src.entity.artifact_entity import PrepareBaeModelArtifact
import os,sys
import tensorflow as tf 
from pathlib import Path

class PrepareBaseModel:
    def __init__(self,prepare_base_model_config: PrepareBaseModelConfig):
        try:
            self.prepare_base_model_config = prepare_base_model_config
            os.makedirs(self.prepare_base_model_config.root_dir,exist_ok=True)
        except Exception as e:
            logging.error(f"Prepare base model object inititation interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
    
    @staticmethod
    def save_model(path: Path,model:tf.keras.Model):
        try:
            logging.info(f"Saving model in path : {path}")
            model.save(path)
        except Exception as e:
            logging.error(f"Model savinginterrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)

    def get_base_model(self):
        try:
            logging.info(f"Making base model for training")
            self.model = tf.keras.applications.vgg16.VGG16(
                input_shape =self.prepare_base_model_config.params_image_size,
                weights = self.prepare_base_model_config.params_weights,
                include_top = self.prepare_base_model_config.params_include_top
            )

            os.makedirs(os.path.dirname(self.prepare_base_model_config.base_model_filepath),exist_ok=True)
            self.save_model(path=self.prepare_base_model_config.base_model_filepath, model=self.model)
            
            return self.prepare_base_model_config.base_model_filepath

        except Exception as e:
            logging.error(f"Getting base model Interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        try:
            logging.info(f"Preparing full model")
            if freeze_all:
                model.trainable = False
            elif (freeze_till is not None) and (freeze_till>0):
                for layer in model.layers[:-freeze_till]:
                    layer.trainable = False
    
            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation = "softmax"
            )(flatten_in)

            full_model = tf.keras.models.Model(
                inputs=model.input,
                outputs=prediction
            )

            full_model.compile(
                optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss = tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"]
            )

            logging.info(f"Full Model summary is as \n {full_model.summary()}")
            return full_model

        except Exception as e:
            logging.error(f"Preparing full base model Interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)

    def update_base_model(self):
        try:
            logging.info(f"Updating base model ")
            self.full_model = self._prepare_full_model(
                model=self.model,
                classes=self.prepare_base_model_config.params_classes,
                freeze_all = True,
                freeze_till=None,
                learning_rate=self.prepare_base_model_config.params_learning_rate
            )

            logging.info(f"saving updated prepared base model ")
            os.makedirs(os.path.dirname(self.prepare_base_model_config.updated_base_model_filepath),exist_ok=True)
            self.save_model(path=self.prepare_base_model_config.updated_base_model_filepath,model=self.full_model)
            
            return self.prepare_base_model_config.updated_base_model_filepath
        except Exception as e:
            logging.error(f"Updating base model Interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)

    def inititate_get_prepare_base_model(self)->PrepareBaeModelArtifact:
        try:
            logging.info(f"{'=='*20} Starting get prepared base model component {'=='*20}")
            base_model_path = self.get_base_model()
            updated_base_model_path = self.update_base_model()

            preparebasemodelartifacts= PrepareBaeModelArtifact(base_model_filepath=base_model_path,
            updated_base_model_filepath=updated_base_model_path)
            logging.info(f"Prepared base model artifacts: {preparebasemodelartifacts}")
            logging.info(f"{'=='*20} Ending get prepared base model component {'=='*20}")
            return preparebasemodelartifacts
        except Exception as e:
            logging.error(f"Initiating getting base model Interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
