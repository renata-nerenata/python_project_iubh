from src.data.load_data import load_data
from src.visualization.visualize import (
    vizualize,
    vizualize_with_points,
    vizualize_ideal,
)
from src.utils import find_all_ideal, test_ideal
from src.data.data_perpesentation import init_data, init_ideal
import pandas as pd
from src.data.final_data_format import final_data
from database.push_data import df_to_sql


def main():
    test = load_data("data/test.csv")
    train = load_data("data/train.csv")
    ideal = load_data("data/ideal.csv")

    # Push data to database
    df_to_sql(train, "training")
    df_to_sql(ideal, "ideal")

    # Change names of the columns in train dataset
    train.columns = [
        column + "_train" if column != "x" else "x" for column in train.columns
    ]

    # Input data vizualization
    vizualize(train)

    # Initialize data as Data object
    list_of_func = init_data(train)

    # Find all ideals function and initialization
    ideals_y = find_all_ideal(ideal, train)
    list_of_func = init_ideal(ideal, list_of_func, ideals_y)

    # Ideal data vizualization
    vizualize_ideal(list_of_func)

    # Test for ideal
    for y in list_of_func:
        y.mapping = test_ideal(test, train, ideal, y.y_label, y.ideal_label)

    # the ideal points on train data vizualization
    vizualize_with_points(list_of_func)

    y1, y2, y3, y4 = list_of_func

    delta = pd.DataFrame(
        [y1.mapping.delta, y2.mapping.delta, y3.mapping.delta, y4.mapping.delta]
    ).max()

    match = pd.DataFrame(
        [y1.mapping.matched, y2.mapping.matched, y3.mapping.matched, y4.mapping.matched]
    ).sum()

    final_dataframe = final_data(test, delta, match)
    df_to_sql(final_dataframe, "final")


if __name__ == "__main__":
    main()
