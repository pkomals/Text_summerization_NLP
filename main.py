from TextSummaizer.pipeline.stage_1_data_ingestion import DataIngestionTrainigPipeline

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
