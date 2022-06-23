import sqlite3


def df_to_sql(dataframe, name_of_table):
    try:
        dbcon = sqlite3.connect("db.sqlite")
    except Exception as err:
        raise SQLError(err)
    dataframe.to_sql(
        name_of_table,
        con=dbcon,
        if_exists="replace",
        index=True,
    )
