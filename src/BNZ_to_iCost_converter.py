import os

import pandas as pd


def create_template_data_frame(headers) -> pd.DataFrame:
    """
    Create a template data frame with the given column headers.

    :param headers: A list of column headers for the data frame.
    :type headers: list or None
    :return: A data frame with the specified column headers.
    :rtype: pd.DataFrame
    :raises TypeError: If the headers parameter is None.
    """
    if headers is None:
        raise TypeError("Headers cannot be None")

    return pd.DataFrame(columns=headers)


def extract_bnz_columns(bnz_file_path, columns: list[str]) -> dict:
    """
    Extracts specified columns from a BNZ data frame.

    :param bnz_file_path: The path to the BNZ data file.
    :param columns: The list of columns to extract.
    :return: A dictionary mapping column names to their corresponding data.
    :raises KeyError: If any of the specified columns do not exist in the BNZ data frame.
    """
    bnz_data_frame = pd.read_csv(bnz_file_path)

    column_datas = dict()
    for column in columns:
        if column not in bnz_data_frame.columns:
            raise KeyError(f"Column '{column}' does not exist in the BNZ data frame")

        column_datas[column] = bnz_data_frame[column]

    return column_datas


def write_columns(serieses: dict, template_data_frame):
    """
    Add columns to the template_data_frame based on the serieses dictionary.

    :param serieses: A dictionary of serieses where the keys are the column headers and the values are the serieses.
    :type serieses: dict
    :param template_data_frame: The template DataFrame to which the columns will be added.
    :type template_data_frame: DataFrame
    :return: None
    """
    for header in serieses:
        template_data_frame[header] = serieses[header]


def write_to_csv(populated_df: pd.DataFrame, dst_path: str):
    """
    Write the given pandas DataFrame to a CSV file.

    :param populated_df: The pandas DataFrame to be written to CSV.
    :param dst_path: The destination path for the CSV file.
    :return: None

    :raises FileNotFoundError: If the directory specified in dst_path does not exist.
    """
    dir_name = os.path.dirname(dst_path)
    if not os.path.exists(dir_name):
        raise FileNotFoundError(f"Directory '{dir_name}' does not exist")

    populated_df.to_csv(dst_path, index=False, header=True)
