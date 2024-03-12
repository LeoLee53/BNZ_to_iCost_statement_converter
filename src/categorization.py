import pandas as pd


def add_entry_type(data_frame: pd.DataFrame):
    """
    Add entry type to each row in the given data frame based on the 'Amount' column.

    :param data_frame: The data frame to add entry type to.
    :type data_frame: pd.DataFrame
    :raises KeyError: If the 'Amount' column is not found in the data frame.
    """
    if 'Amount' not in data_frame.columns:
        raise KeyError('column Amount not found in dataframe')

    for index in data_frame.index:
        if data_frame.loc[index, 'Amount'] < 0:
            data_frame.loc[index, 'Type'] = 'Expense'
