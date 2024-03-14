import os

import pandas as pd
from pandas import to_datetime

from src.config import *


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


def extract_bnz_columns(bnz_file_path, headers: list[str]) -> dict[str, pd.Series]:
    """
    Extracts specified columns from a BNZ data frame.

    :param bnz_file_path: The path to the BNZ data file.
    :param headers: The list of columns to extract.
    :return: A dictionary mapping column names to their corresponding data.
    :raises KeyError: If any of the specified columns do not exist in the BNZ data frame.
    """
    bnz_data_frame = pd.read_csv(bnz_file_path)

    column_datas = dict()
    for header in headers:
        if header not in bnz_data_frame.columns:
            raise KeyError(
                f"Header '{header}' does not exist in the BNZ data frame")

        ch_header = ENG_TO_CN_HEADER_MAP[header]
        column_datas[ch_header] = bnz_data_frame[header]

    return column_datas


def populate_template_dataframe(serieses: dict, template_data_frame):
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


def format_date(populated_df):
    """
    :param populated_df: The pandas DataFrame that contains the column "日期" which represents dates as strings in the format dd/mm/yy.
    :return: The pandas DataFrame with the dates in the column "日期" formatted as strings in the format yyyy/mm/dd.

    Example usage:

    >>> df = pd.DataFrame({"日期": ["01/01/22", "02/02/22"]})
    >>> format_date(df)
    >>> print(df)
          日期
    0  2022/01/01
    1  2022/02/02

    """
    populated_df["日期"] = to_datetime(populated_df["日期"], format="%d/%m/%y").dt.strftime("%Y/%m/%d")


def format_amount(populated_df: pd.DataFrame):
    """
    :param populated_df: A pandas DataFrame with a column named '金额', representing amounts.
    :return: None

    This method formats the amounts in the '金额' column of the provided DataFrame. It takes each value in the column, converts it to a float, and takes the absolute value. The formatted values
    * are then updated in the DataFrame inplace.
    """
    for index in populated_df.index:
        populated_df.at[index, "金额"] = abs(float(populated_df.at[index, '金额']))


def format_account(populated_df: pd.DataFrame):
    """
    Formats the account values in the given DataFrame to be absolute value.

    :param populated_df: A pandas DataFrame containing the account information.
    :return: None

    The method formats the account values in the '账户1' and '账户2' columns of the DataFrame
    according to the BNZ_TO_ICOST_ACCOUNT_MAP dictionary. The updated values are stored back
    in the DataFrame.
    """
    for index in populated_df.index:
        populated_df.at[index, '账户1'] = BNZ_TO_ICOST_ACCOUNT_MAP[populated_df.at[index, '账户1']]

        if populated_df.at[index, '账户2'] in BNZ_TO_ICOST_ACCOUNT_MAP.keys():
            populated_df.at[index, '账户2'] = BNZ_TO_ICOST_ACCOUNT_MAP[populated_df.at[index, '账户2']]


def add_currency(populated_df: pd.DataFrame, currency: str):
    """
    Add currency abbreviation to the currency column of the template dataframe.

    :param populated_df: The DataFrame to add the currency column to.
    :param currency: The currency value to assign to each row in the DataFrame.
    :return: The DataFrame with the added currency column.
    """
    populated_df["货币"] = currency


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
