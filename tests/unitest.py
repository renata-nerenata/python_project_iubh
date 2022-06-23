import unittest

from src.models.evaluation_score import squared_error
from src.utils import find_ideal
from src.data.load_data import load_data


class TestScoreMethods(unittest.TestCase):

    test = load_data("data/test.csv")
    train = load_data("data/train.csv")
    ideal = load_data("data/ideal.csv")

    train.columns = [
        column + "_train" if column != "x" else "x" for column in train.columns
    ]

    def test_score(self):
        self.assertEqual(squared_error(2, 3), 1)

    def test_find_ideal(self, ideal, train):
        self.assertEqual(find_ideal(ideal, train, "y1_train"), "y46")
        self.assertEqual(find_ideal(ideal, train, "y2_train"), "y16")


if __name__ == "__main__":
    unittest.main()
