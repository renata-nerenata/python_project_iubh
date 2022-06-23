from sqlalchemy import Table, Column, Integer, MetaData, Float


def create_pattern(NAME_OF_TABLE, metadata, number_y):

    columns_names = ["X"]

    for i in range(number_y):
        columns_names.append("Y{} ({} function)".format(i + 1, NAME_OF_TABLE))

    columns_types = [Float] * (number_y + 1)
    primary_key_flags = [True] + [False] * number_y
    nullable_flags = [False] * (number_y + 1)

    table = Table(
        NAME_OF_TABLE,
        metadata,
        *(
            Column(
                column_name,
                column_type,
                primary_key=primary_key_flag,
                nullable=nullable_flag,
            )
            for column_name, column_type, primary_key_flag, nullable_flag in zip(
                columns_names, columns_types, primary_key_flags, nullable_flags
            )
        )
    )
    return table


def create_final_pattern(NAME_OF_TABLE, metadata):
    columns_names = [
        "X (test func)",
        "Y (test func)",
        "Delta Y (test func)",
        "No. of ideal func",
    ]
    columns_types = [Float] * 4
    primary_key_flags = [True] + [False] * 3
    nullable_flags = [False] * 4
    table = Table(
        NAME_OF_TABLE,
        metadata,
        *(
            Column(
                column_name,
                column_type,
                primary_key=primary_key_flag,
                nullable=nullable_flag,
            )
            for column_name, column_type, primary_key_flag, nullable_flag in zip(
                columns_names, columns_types, primary_key_flags, nullable_flags
            )
        )
    )
    return table
