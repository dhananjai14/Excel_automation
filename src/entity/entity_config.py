import os
import sys
from datetime import datetime
from src.exception import ExcelException
from src.logger import logging


class InitiatePipeConfig:
    def __init__(self):
        try:
            logging.info('>>>>>>>>>>> Inside class: InitiatePipeConfig <<<<<<<<<<<<')
            dir_name = datetime.now().strftime("%m-%d-%Y__%H%M%S")
            self.artifact_dir = os.path.join(os.getcwd(), 'artifact', dir_name)
            os.makedirs(self.artifact_dir, exist_ok=True)
            logging.info(f'Directory created: {self.artifact_dir}')
            logging.info('>>>>>>>>>>> Exit from class: InitiatePipeConfig <<<<<<<<<<<<')
        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)


class DataIngestionConfig:
    def __init__(self, initiate_pipe_config: InitiatePipeConfig):
        try:
            logging.info(f'{">>" * 20} Inside the Class: DataIngestionConfig {"<<" * 20}')
            self.input_file_path = os.path.join(os.getcwd(), 'Input')
            self.template_file_path = os.path.join(os.getcwd(), 'Template')
            self.data_ingestion_input = os.path.join(initiate_pipe_config.artifact_dir, 'data_ingestion', 'input')
            self.data_ingestion_template = os.path.join(initiate_pipe_config.artifact_dir, 'data_ingestion', 'template')
            logging.info(f'{">>" * 20} Exit Class: DataIngestionConfig {"<<" * 20}')

        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)

    def to_dict(self):
        try:
            self.__dict__
        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)


class DataValidationConfig:
    def __init__(self, initiate_pipe_config: InitiatePipeConfig):
        try:
            logging.info(f'{">>" * 20} Inside the Class: DataValidationConfig {"<<" * 20}')
            self.data_validation_dir = os.path.join(initiate_pipe_config.artifact_dir, 'data_validation')
            self.data_validation_input = os.path.join(self.data_validation_dir, 'input')
            self.data_validation_temp = os.path.join(self.data_validation_dir, 'template')
            self.report_file_path = os.path.join(self.data_validation_dir, 'report.yaml')
            self.sample_input_location = os.path.join(os.getcwd(), 'Sample_Input')
            logging.info(f'{">>" * 20} Exit Class: DataValidationConfig {"<<" * 20}')
        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)


class DataCalculationConfig:
    def __init__(self, initiate_pipe_config: InitiatePipeConfig):
        try:
            logging.info(f'{">>" * 20} Inside the Class: DataCalculationConfig {"<<" * 20}')
            self.data_calculation_dir = os.path.join(initiate_pipe_config.artifact_dir, 'data_calculation')
            logging.info(f'{">>" * 20} Exit the Class: DataCalculationConfig {"<<" * 20}')
        except Exception as e:
            raise ExcelException(e, sys)


class OutputGenerationConfig:
    def __init__(self):
        try:
            logging.info(f'{">>" * 20} Inside the Class: OutputGenerationConfig {"<<" * 20}')
            self.output_dir = os.path.join(os.getcwd(), 'Output')
            logging.info(f'{">>" * 20} Exit the Class: OutputGenerationConfig {"<<" * 20}')
        except Exception as e:
            raise ExcelException(e, sys)
