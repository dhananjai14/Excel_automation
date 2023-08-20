from dataclasses import dataclass


@dataclass
class InputFileName:
    input_file1 = 'Input.xlsx'
    template_file = 'Template.xlsx'


input_file = InputFileName()
input_file_list = [input_file.input_file1]
template_file = input_file.template_file


@dataclass
class InputProperties:
    input_file_sheet1 = ['Input']
    template_file_sheets = ['Input', 'Output']
    columns_count_input_1 = [4]


sheets = InputProperties
input_sheet_list = [InputProperties.input_file_sheet1]
template_sheet_list = InputProperties.template_file_sheets
column_list = [InputProperties.columns_count_input_1]


@dataclass
class OutputFileName:
    output_file1 = 'Sales.xlsx'


output_file = OutputFileName()
output_file_name = output_file.output_file1


@dataclass
class SheetMapping:
    sheet_mapping = {InputFileName.input_file1: {'Input': 'Input'}}
