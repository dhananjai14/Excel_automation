import os
import sys
from src import utils
from src.logger import logging
from src.exception import ExcelException
from src.entity import entity_artifact, entity_config
from datetime import datetime
from src import properties


class OutputGeneration:
    def __init__(self, output_gen_config: entity_config.OutputGenerationConfig,
                 data_calculation_artifact: entity_artifact.DataCalculationArtifact):
        try:
            logging.info(f"{'>>' * 20} Inside class: OutputGeneration {'<<' * 20}")
            self.output_gen_config = output_gen_config
            self.data_calculation_artifact = data_calculation_artifact
            logging.info('OutputGeneration Initiation completed')
        except Exception as e:
            raise ExcelException(e, sys)

    def execute(self):
        try:
            logging.info(f"{'>>' * 20} Inside Method: DataCalculation.execute {'<<' * 20}")
            output_file_name = properties.output_file_name.split('.')
            current_date_time = datetime.now().strftime("%m-%d-%Y__%H%M%S")
            output_file_name.insert(-1, '_')
            output_file_name.insert(-1, current_date_time)
            output_file_name.insert(-1, '.')
            output_file = ''.join(output_file_name)
            logging.info(f'Output file name: {output_file}')

            output_path = os.path.join(self.output_gen_config.output_dir, output_file)
            logging.info(f'Output file path: {output_path}')

            temp_output_file = self.data_calculation_artifact.temp_output_file
            utils.file_operation(source_file=temp_output_file, destination_file=output_path, operation='copy')

            logging.info('Output generation entity created')
            output_artifact = entity_artifact.Output(output_file_path=output_path)
            logging.info('Output file generated')
            return output_artifact

        except Exception as e:
            raise ExcelException(e, sys)
