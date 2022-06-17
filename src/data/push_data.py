import pandas as pd
from sqlalchemy import create_engine


class SQL_error(Exception):
    pass


def to_sql(dataframe, filename, suffix):
    """
    Push the dataframe into a local sqlite db
    :param dataframe: data to push to dababase
    :param filename: name of dataframe
    :param suffix: a specific suffix
    """
    engine = create_engine('sqlite:///{}.db'.format(filename), echo=False)

    dataframe_tosql = dataframe.copy()
    dataframe_tosql.columns = [column.capitalize() + suffix for column in dataframe_tosql.columns]

    try:
        dataframe_tosql.to_sql(
            filename,
            engine,
            if_exists="replace",
            index=True,
        )

    except Exception as err:
        raise SQL_error(err)
