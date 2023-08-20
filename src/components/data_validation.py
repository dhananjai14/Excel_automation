import os
import shutil
import sys
import pandas as pd
from src.entity import entity_config, entity_artifact
from src.exception import ExcelException
from src.logger import logging
from src import properties
from src.utils import file_operation


class DataValidation:
    def __init__(self, data_ingestion_artifact: entity_artifact.DataIngestionArtifact,
                 data_validation_config: entity_config.DataValidationConfig):
        try:
            logging.info(f"{'>>' * 20} Inside class: DataValidation {'<<' * 20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.validation_error = dict()
            logging.info('DataValidation Initiation completed')

        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)

    def execute(self):
        try:
            logging.info(f"{'>>' * 20} Inside Method: DataValidation.execute {'<<' * 20}")
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            os.makedirs(self.data_validation_config.data_validation_temp, exist_ok=True)
            os.makedirs(self.data_validation_config.data_validation_input, exist_ok=True)
            input_path_lst = self.data_ingestion_artifact.input_file_path_list
            ref_sheet_list = properties.input_sheet_list

            logging.info('Validating if all sheets in input files are present')
            for i in range(len(input_path_lst)):
                if self.sheet_match(input_file_path=input_path_lst[i], ref_sheets_list=ref_sheet_list[i]) is True:
                    pass
                else:
                    raise Exception('Sheet mismatch observed for input files')
            logging.info('All sheets are in place for input files')

            logging.info('Validating if all the sheets in template files are present ')
            if self.sheet_match(input_file_path=self.data_ingestion_artifact.template_file_path,
                                ref_sheets_list=properties.template_sheet_list) is True:
                valid_temp_path = os.path.join(self.data_validation_config.data_validation_temp
                                               , os.path.basename(self.data_ingestion_artifact.template_file_path))
                file_operation(source_file=self.data_ingestion_artifact.template_file_path
                               , destination_file=valid_temp_path, operation='move')
            else:
                raise Exception('Sheet mismatch observed for template files')
            logging.info('All sheets are in place for template files')

            logging.info('Validating input columns')
            valid_input_path_lst = []
            for i in range(len(properties.column_list)):
                column_list = properties.column_list[i]
                sheet_list = properties.input_sheet_list[i]
                input_path = input_path_lst[i]
                for j in range(len(column_list)):
                    df = pd.read_excel(input_path, sheet_name=sheet_list[j])
                    if df.shape[1] == column_list[j]:
                        logging.info(f'Sheet: {sheet_list[j]} has {column_list[j]} number of columns')
                    else:
                        raise Exception(f'Sheet: {sheet_list[j]} has {df.shape[1]} column and required'
                                        f' columns are {column_list[j]} in input file {os.path.basename(input_path)}')
                valid_input_path = os.path.join(self.data_validation_config.data_validation_input
                                                , os.path.basename(input_path_lst[i]))
                file_operation(source_file=input_path_lst[i], destination_file=valid_input_path,
                               operation='move')
                valid_input_path_lst.append(valid_input_path)
            logging.info('All columns are in place for input')

            data_validation_artifact = entity_artifact.DataValidationArtifact(
                valid_input_path_list=valid_input_path_lst,
                valid_template_path=valid_temp_path)
            logging.info(f'Data Validation Artifact created: {data_validation_artifact}')
            logging.info(f"{'>>' * 20} Exit Method: DataValidation.execute {'<<' * 20}")
            return data_validation_artifact
        except Exception as e:
            logging.error(e)
            raise ExcelException(e, sys)

    def sheet_match(self, input_file_path: os.path, ref_sheets_list: list):
        logging.info('Sheet Match initiated')
        logging.info(f'Looking for sheets: {ref_sheets_list} in input file {os.path.basename(input_file_path)}')
        df = pd.read_excel(input_file_path, None)
        logging.info(f'Input file picked {input_file_path}')
        sheet_list_input = list(df.keys())
        if sorted(sheet_list_input) != sorted(ref_sheets_list):
            missing_sheets = list(set(ref_sheets_list) - set(sheet_list_input))
            raise Exception(f'Reference Sheets: {missing_sheets} is not present '
                            f'in input file {os.path.basename(input_file_path)}')
        else:
            logging.info(f'Reference Sheets: {ref_sheets_list} present in input'
                         f' file {os.path.basename(input_file_path)}')
        return True
