from TextSummaizer.pipeline.stage_1_data_ingestion import DataIngestionTrainigPipeline

from TextSummaizer.pipeline.stage_2_data_validation import DataValidationTrainigPipeline

from TextSummaizer.pipeline.stage_3_data_transformation import DataTransformationTrainigPipeline

from TextSummaizer.pipeline.stage_4_model_trainer import ModelTrainerTrainingPipeline

from TextSummaizer.logging import logger
from TextSummaizer.config.configuration import CONFIG_FILE_PATH
from TextSummaizer.config.configuration import ConfigurationManager
import os
import sys

# print(f"🛠️ Current working directory: {os.getcwd()}")
# print(f"🔍 Python is searching for modules in: {sys.path}")

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   print(f"🔍 CONFIG_FILE_PATH from constant: {CONFIG_FILE_PATH.resolve()}")
   config_manager = ConfigurationManager()
   data_ingestion = DataIngestionTrainigPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   #print(f"🔍 CONFIG_FILE_PATH from constant: {CONFIG_FILE_PATH.resolve()}")
   config_manager = ConfigurationManager()
   data_validation = DataValidationTrainigPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainigPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e