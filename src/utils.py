import pandas as pd
from src.models.evaluation_score import squared_error
import functools as ft
import numpy as np
from CONSTANTS import tolerance, trained_list


def find_ideal(ideal, train, y_label):
    """
    :param ideal:
    :param train:
    :param y_label:
    :return:
    """
    squared_deviations = pd.DataFrame()

    for column in ideal.columns:
        squared_deviations[column] = squared_error(train[y_label], ideal[column])

    return squared_deviations.sum(axis=0).idxmin()


def find_all_ideal(ideal, train):
    """
    :param ideal:
    :param train:
    :return:
    """
    ideals_y = {}
    for y_label in trained_list:
        ideals_y[y_label] = find_ideal(ideal, train, y_label)

    return ideals_y



def test_ideal(test, train, ideal, y_label, ideal_label):
    """
    :param test:
    :param train:
    :param ideal:
    :param y_label:
    :param ideal_label:
    :return:
    """
    try:
        dfs = [test, train, ideal[["x", ideal_label]]]
        data = ft.reduce(lambda left, right: pd.merge(left, right, on="x"), dfs)

        delta_label = "delta"
        match_label = "matched"

        data[delta_label] = np.abs(data[ideal_label] - data["y"]) - tolerance * np.abs(
            data[y_label] - data[ideal_label]
        )
        data[match_label] = data[delta_label] <= 0

        mapping = data[["x", "y", ideal_label, delta_label, match_label]]
        return mapping

    except Exception as e:
        print("Error! Code: {c}, Message, {m}".format(c=e.code, m=str(e)))


def get_points(mapping, y_label):
    match_label = y_label + "_matched"

    x_points = mapping[mapping[match_label] == True]["x"]
    y_points = mapping[mapping[match_label] == True]["y"]

    return x_points, y_points
