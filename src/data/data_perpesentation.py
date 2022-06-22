from CONSTANTS import trained_list


class Data(object):
    def __init__(self, x, y_label=None, ideal_label=None):
        self.x = x
        self.y_label = y_label
        self.ideal_label = ideal_label

    def sign_y_train(self, train):
        self.y_train = train[self.y_label]

    def sign_y_ideal(self, ideal):
        self.y_ideal = ideal[self.ideal_label]


def init_data(train, trained_list=trained_list):

    y1 = Data(train["x"], y_label=trained_list[0])
    y2 = Data(train["x"], y_label=trained_list[1])
    y3 = Data(train["x"], y_label=trained_list[2])
    y4 = Data(train["x"], y_label=trained_list[3])

    list_of_func = [y1, y2, y3, y4]

    for y in list_of_func:
        y.sign_y_train(train)

    return y1, y2, y3, y4


def init_ideal(ideal, list_of_func, ideals_y):
    for y in list_of_func:
        y.ideal_label = ideals_y[y.y_label]
        y.sign_y_ideal(ideal)

    return list_of_func
