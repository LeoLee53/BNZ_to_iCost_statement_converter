import pandas as pd

from src.config import BNZ_TO_ICOST_ACCOUNT_MAP


def add_entry_type(data_frame: pd.DataFrame):
    """
    Adds an entry type to each row in the given DataFrame.

    Parameters:
    - data_frame (pd.DataFrame): The DataFrame containing the entries.

    Returns:
    - None
    """
    for index in data_frame.index:
        entry_type = _decide_entry_type(data_frame, index)
        _change_account_order(data_frame, index)
        _clean_up_income_bills(data_frame, index, entry_type)

        data_frame.at[index, '类型'] = entry_type


def _clean_up_income_bills(data_frame, index, entry_type):
    if entry_type == '收入':
        data_frame.at[index, '账户1'] = data_frame.at[index, '账户2']
        data_frame


def _change_account_order(data_frame, index):
    """
    Swaps the values of '账户1' and '账户2' columns in the specified row of the given DataFrame.

    Args:
        data_frame (pandas.DataFrame): The DataFrame containing the account information.
        index (int): The index of the row to be modified.

    Returns:
        None
    """
    if data_frame.at[index, '金额'] > 0:
        temp = data_frame.at[index, '账户1']
        data_frame.at[index, '账户1'] = data_frame.at[index, '账户2']
        data_frame.at[index, '账户2'] = temp


def _decide_entry_type(data_frame, index):
    """
    Determines the type of entry based on the account and amount.

    Args:
        data_frame (pandas.DataFrame): The DataFrame containing the entry data.
        index (int): The index of the entry in the DataFrame.

    Returns:
        str: The type of entry ('支出', '收入', or '转账').

    """
    account2 = data_frame.at[index, '账户2']
    amount = data_frame.at[index, '金额']

    if account2 == '---':
        entry_type = '支出'
    elif not _is_my_account(account2):
        entry_type = '收入' if amount > 0 else '支出'
    else:
        entry_type = '转账'

    return entry_type


def _is_my_account(account2):
    """
    Checks if the given account is one of my accounts, either formatted or not.

    Args:
        account2 (str): The account to check.

    Returns:
        bool: True if the account is found in either the original accounts or the formatted accounts, False otherwise.
    """
    original_accounts = BNZ_TO_ICOST_ACCOUNT_MAP.keys()
    formatted_accounts = BNZ_TO_ICOST_ACCOUNT_MAP.values()
    return account2 in original_accounts or account2 in formatted_accounts
