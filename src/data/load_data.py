import pandas as pd
from src.exception import EmptyX, EmptyY, DataFormatError, CustomError


def check_data_content(data):
    """
    Check data have x and y features
    :param data:
    :return:
    """
    if "x" not in data.columns:
        raise EmptyX(data)
    if len(data.columns) < 2:
        raise EmptyY(data)


def check_data_type(data):
    """
    Check that all data is numerical
    :param data:
    :return:
    """
    if data.shape != data._get_numeric_data().shape:
        raise DataFormatError(data)


def load_data(filepath):
    """
    Parse local .csv file
    :param filepath:
    :return: dataframe from .scv file
    """
    try:
        data = pd.read_csv(filepath)
        check_data_content(data)
        check_data_type(data)
        return data
    except FileNotFoundError:
        raise CustomError("There is no a file")
