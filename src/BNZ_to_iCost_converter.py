import pandas as pd


def create_template_dataframe(headers) -> pd.DataFrame:
    if headers == None:
        raise TypeError("Headers cannot be None")

    return pd.DataFrame(columns=headers)


def extract_bnz_columns(bnz_file_path, columns: list[str]) -> dict:
    data_frame = pd.read_csv(bnz_file_path)

    column_datas = dict()
    for column in columns:
        column_datas[column] = data_frame[column]

    return column_datas


def write_columns(serieses: list[pd.Series], template_data_frame):
    for series in serieses:
        if series.name is None:
            raise AttributeError("Series must have a name")
        template_data_frame[series.name] = series
