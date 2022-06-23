import unittest

from src.models.evaluation_score import squared_error


class TestScoreMethods(unittest.TestCase):
    def test_score(self):
        self.assertEqual(squared_error(2, 3), 1)


if __name__ == "__main__":
    unittest.main()
