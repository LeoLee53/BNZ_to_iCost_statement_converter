from src.config import HEADERS
from src.CSV_manupulation import add_currency, create_template_data_frame, extract_bnz_columns, format_account, format_amount, format_date, populate_template_dataframe
from src.categorization import add_entry_type
import pandas as pd


def main(dst_path):
    """
    A wrapper function that gathers all operations needed for bill conversion in a single place and make sure
    they happen in the right order.

    Args:
        dst_path (str): The destination file path where the converted statement will be saved.

    Returns:
        None
    """

    df = pd.DataFrame(columns=HEADERS)
    series = extract_bnz_columns('test_materials/BNZ.csv',
                                 ['Date', 'Amount', 'This Party Account', 'Other Party Account', 'Payee'])

    populate_template_dataframe(series, df)

    format_date(df)

    format_account(df)

    add_entry_type(df)

    format_amount(df)

    add_currency(df, 'NZD')

    df.to_csv(dst_path, index=False)


main('test_materials/test.csv')
