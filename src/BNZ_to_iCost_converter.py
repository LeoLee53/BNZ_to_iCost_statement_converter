import pandas as pd


def create_template_dataframe(headers) -> pd.DataFrame:
    if headers is None:
        raise TypeError("Headers cannot be None")

    return pd.DataFrame(columns=headers)


def extract_bnz_columns(bnz_file_path, columns: list[str]) -> dict:
    bnz_data_frame = pd.read_csv(bnz_file_path)

    column_datas = dict()
    for column in columns:
        if column not in bnz_data_frame.columns:
            raise KeyError(f"Column '{column}' does not exist in the BNZ data frame")

        column_datas[column] = bnz_data_frame[column]

    return column_datas


def write_columns(serieses: dict, template_data_frame):
    for header in serieses:
        template_data_frame[header] = serieses[header]
