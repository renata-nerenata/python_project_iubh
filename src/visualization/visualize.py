import matplotlib.pyplot as plt
from src.utils import get_points


def fig_saver(y_label, path="reports/figures/"):
    """
    :param y_label: Name of y
    :param path: Path for figures
    :return:
    """
    filename = path + y_label + ".png"
    plt.savefig(filename, dpi=300)


def scatter_plot(x, y, y_label):
    """
    :param x: Given x
    :param y: Given y
    :param y_label: Name of y
    :return: scatter plot
    """
    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel(y_label)
    fig_saver('Initial ' + y_label)


def scatter_plot_with_points(x, y, x_points, y_points, y_label):
    """
    :param x: Given x
    :param y: Given y
    :param n_points: Number of mapped points
    :param x_points: x coordinate of mapped point
    :param y_points: y coordinate of mapped point
    :param y_label: Label of y
    :return: scatter plot with mapped points
    """
    plt.figure()
    plt.scatter(x, y)
    plt.scatter(x_points, y_points)
    plt.legend(
        [y_label, "Points"],
        ncol=2,
        loc="best",
    )
    plt.title("Number of points: " + str(len(x_points)))
    plt.xlabel("x")
    plt.ylabel("Ideal function for " + y_label)
    fig_saver('With test ' + y_label)


def vizualize(data):
    for column in data.columns.difference(["x"]):
        scatter_plot(data["x"], data[column], column)


def vizualize_with_points(list_of_func):

    for y in list_of_func:
        x_points, y_points = get_points(y.mapping, y.y_label)
        scatter_plot_with_points(
            y.x, y.y_ideal, x_points, y_points, y.y_label
        )
