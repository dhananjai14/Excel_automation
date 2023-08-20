from src.logger import logging
import os
from src.components import data_ingestion
from src.entity import entity_config
from src.components import data_validation
from src.components import data_calculation
from src.components import output_generation

if __name__ == "__main__":
    # Data initialisation
    initiate_pipe = entity_config.InitiatePipeConfig()

    # Data Ingestion
    data_ingestion_config = entity_config.DataIngestionConfig(initiate_pipe_config=initiate_pipe)
    data_ingestion = data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
    data_ingestion_artifact = data_ingestion.execute()

    # Data Validation
    data_validation_config = entity_config.DataValidationConfig(initiate_pipe_config=initiate_pipe)
    data_validation = data_validation.DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                                     data_validation_config=data_validation_config)
    data_validation_artifact = data_validation.execute()

    # Data Calculation
    data_calculation_config = entity_config.DataCalculationConfig(initiate_pipe_config=initiate_pipe)
    data_calculation = data_calculation.DataCalculation(data_validation_artifact = data_validation_artifact,
                                                        data_calculation_config=data_calculation_config)
    data_calculation_artifact = data_calculation.execute()

    # Output generation
    output_generation_config = entity_config.OutputGenerationConfig()
    output_generation = output_generation.OutputGeneration(output_gen_config=output_generation_config,
                                                           data_calculation_artifact = data_calculation_artifact)
    output_artifact = output_generation.execute()

    # Output file location
    logging.info(f'Output file generated at: {output_artifact.output_file_path}')





