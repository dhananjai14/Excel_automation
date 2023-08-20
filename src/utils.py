import os.path
import shutil
import sys
from src.logger import logging
from src.exception import ExcelException
import pandas as pd


def file_operation(source_file: os.path, destination_file: os.path, operation='copy'):
    try:
        logging.info(f'{operation} file initiated from {source_file} to {destination_file}')
        if operation == 'copy':
            if os.path.exists(destination_file):
                os.remove(destination_file)
            shutil.copyfile(source_file, destination_file)
        if operation == 'move':
            shutil.move(source_file, destination_file)
        logging.info(f'{operation} file completed from {source_file} to {destination_file}')
    except Exception as e:
        logging.error(e)
        raise ExcelException(e, sys)


def get_sheet_names( excel_file_path:os.path):
    try:
        logging.info('Sheet Extraction initiated')
        df = pd.read_excel(excel_file_path, None)
        sheet_list = list(df.keys())
        logging.info(f'Input {excel_file_path} has sheets: {sheet_list}')
        return sheet_list
    except Exception as e:
        raise ExcelException(e, sys)
