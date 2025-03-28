from TextSummaizer.config.configuration import ConfigurationManager
from TextSummaizer.components.data_transformation import DataTransformation
from TextSummaizer.logging import logger

class DataTransformationTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()