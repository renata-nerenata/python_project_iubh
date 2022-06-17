import pandas as pd


def check_data_content(data):
    if "x" not in data.columns:
        print("There is no x parameter")
    if len(data.columns) < 2:
        print("There is no y parameter")
    print('Data is perfect!')


def load_data(filepath):
    """
    Parse local .csv file
    :param filepath:
    :return:
    """
    try:
        data = pd.read_csv(filepath)
        check_data_content(data)

        return data
    except FileNotFoundError:
        print('There is no a file')
