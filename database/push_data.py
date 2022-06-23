import sqlite3
from src.exception import SQLError


def df_to_sql(dataframe, name_of_table):
    try:
        db_engine = sqlite3.connect("db.sqlite")
    except Exception as err:
        raise SQLError(err)
    dataframe.to_sql(
        name_of_table,
        con=db_engine,
        if_exists="replace",
        index=True,
    )
