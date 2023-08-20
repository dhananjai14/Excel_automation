import os
import sys
from src.logger import logging
from src.exception import ExcelException
from src import utils
from src.entity import entity_config
from src.entity import entity_artifact
from src import properties


class DataIngestion:
    def __init__(self, data_ingestion_config: entity_config.DataIngestionConfig):
        try:
            logging.info('>>>>>>>>>>>>>> Inside Class: DataIngestion <<<<<<<<<<<<<')
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)

    def execute(self):
        try:
            logging.info('>>>>>>>>> Inside method: DataIngestion.execute <<<<<<<<<<<')
            logging.info('================== Data Ingestion Initiated =====================')
            data_ingestion_config = self.data_ingestion_config

            if os.path.exists(data_ingestion_config.data_ingestion_input) is True:
                os.remove(data_ingestion_config.data_ingestion_input)
            os.makedirs(data_ingestion_config.data_ingestion_input)
            logging.info(f'Input Directory created: {data_ingestion_config.data_ingestion_input}')

            if os.path.exists(data_ingestion_config.data_ingestion_template) is True:
                os.remove(data_ingestion_config.data_ingestion_template)
            os.makedirs(data_ingestion_config.data_ingestion_template)
            logging.info(f'Template Directory created: {data_ingestion_config.data_ingestion_template}')

            input_files = properties.input_file_list
            logging.info('Input file name Pulled')
            logging.info(f'Input files: {input_files}')
            input_file_path_list = []

            for file in input_files:
                source_path = os.path.join(data_ingestion_config.input_file_path, file)
                logging.info(f'Input file path created: {source_path}')

                if os.path.exists(path=source_path) is not True:
                    raise Exception(f'Input file {file} does not exist in {data_ingestion_config.input_file_path}')

                destination_path = os.path.join(data_ingestion_config.data_ingestion_input, file)
                logging.info(f'Destination file path for Input created: {destination_path}')

                logging.info(f'Input File {file} copy initiated')
                utils.file_operation(source_file=source_path, destination_file=destination_path)
                logging.info(f'Input File {file} copy Finished')

                input_file_path_list.append(destination_path)
            template_source_path = os.path.join(data_ingestion_config.template_file_path, properties.template_file)
            logging.info(f'Template file path created: {template_source_path}')

            template_destination_path = os.path.join(data_ingestion_config.data_ingestion_template,
                                                     properties.template_file)
            logging.info(f'Destination file path for Template created: {template_destination_path}')

            if os.path.exists(template_source_path) is not True:
                raise Exception(f'Template file {properties.template_file} does not '
                                f'at {data_ingestion_config.template_file_path} ')

            logging.info('Template File copy initiated')
            utils.file_operation(template_source_path, template_destination_path)
            logging.info('Template File copy completed')

            data_ingestion_artifact = entity_artifact.DataIngestionArtifact(
                                                                    template_file_path=template_destination_path
                                                                    , input_file_path_list=input_file_path_list)
            logging.info(f'Data Ingestion artifact created: {data_ingestion_artifact}')
            logging.info('>>>>>>>>> Exit method: DataIngestion.execute <<<<<<<<<<<')
            logging.info('================== Data Ingestion Completed =====================')

            return data_ingestion_artifact

        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)
