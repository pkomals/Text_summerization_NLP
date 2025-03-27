from TextSummaizer.config.configuration import ConfigurationManager
from TextSummaizer.components.data_validation import DataValiadtion
from TextSummaizer.logging import logger

class DataValidationTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValiadtion(config=data_validation_config)
        #data_validation.download_file()
        data_validation.validate_all_files_exist()