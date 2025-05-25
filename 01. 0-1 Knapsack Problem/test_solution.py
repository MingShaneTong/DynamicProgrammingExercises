import unittest
from solution import solution
from helper import Item

class TestSolution(unittest.TestCase):
    def test(self):
        capacity = 7
        items = [
            Item(1, 1),
            Item(3, 4),
            Item(4, 5),
            Item(5, 7)
        ]
        expected = [
            Item(3, 4),
            Item(4, 5)
        ]
        observed = solution(capacity, items)
        self.assertCountEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()