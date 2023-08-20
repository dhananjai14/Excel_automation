from dataclasses import dataclass
import os


@dataclass
class DataIngestionArtifact:
    template_file_path: os.path
    input_file_path_list: list


@dataclass
class DataValidationArtifact:
    valid_input_path_list: list
    valid_template_path: os.path


@dataclass
class DataCalculationArtifact:
    temp_output_file: os.path


@dataclass
class Output:
    output_file_path: os.path
