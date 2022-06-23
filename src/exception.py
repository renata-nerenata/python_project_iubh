class EmptyDataError(Exception):
    """
    .csv file is Empty
    """

    def __init__(self, filepath):
        self.filepath = filepath

    def __str__(self):
        return "Error: {} - data is empty. Check your resource".format(self.filepath)


class EmptyX(Exception):
    """
    Dataframe has X feature
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __str__(self):
        return "Error: {} - data is not contain X. Check your resource".format(
            self.filepath
        )


class EmptyY(Exception):
    """
        Dataframe has Y feature
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __str__(self):
        return "Error: {} - data is not contain Y. Check your resource".format(
            self.filepath
        )


class CustomError(Exception):
    pass


class SQLError(Exception):
    pass


class DataFormatError(Exception):
    """
    The data type is not numerical
    """

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "Error: {} contains inappropriate value type".format(self.data)


class NoDataBase(Exception):
    """
    There is no Database
    """

    def __init__(self, database):
        self.database = database

    def __str__(self):
        return "Error: Database is not exist".format(self.database)


class WrongDataName(Exception):
    """
    There is no Database
    """

    def __init__(self, database_name):
        self.database_name = database_name

    def __str__(self):
        return (
            "Error: Database name is inappropriate. It permits only lowercase".format(
                self.database_name
            )
        )


class TypesDataBaseValues(Exception):
    """
    There is no Database
    """

    def __init__(self, database):
        self.database = database

    def __str__(self):
        return "Error: Database is not exist".format(self.database)
