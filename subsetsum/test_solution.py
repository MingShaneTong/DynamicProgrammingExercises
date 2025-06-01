import unittest
from .solution import solution

class TestSolution(unittest.TestCase):
    def test1(self):
        target = 11
        number_set = [2, 3, 7, 8, 10]
        expected = [3, 8]
        observed = solution(target, number_set)
        self.assertCountEqual(expected, observed)
    
    def test2(self):
        target = 14
        number_set = [2, 3, 7, 8, 10]
        expected = []
        observed = solution(target, number_set)
        self.assertCountEqual(expected, observed)

    def test3(self):
        target = 9
        number_set = [3, 34, 4, 12, 5, 2]
        expected = [2, 3, 4]
        observed = solution(target, number_set)
        self.assertCountEqual(expected, observed)

    def test4(self):
        target = 10
        number_set = [3, 34, 4, 12, 5, 2]
        expected = [2, 3, 5]
        observed = solution(target, number_set)
        self.assertCountEqual(expected, observed)

    def test5(self):
        target = 1
        number_set = [2, 3]
        expected = []
        observed = solution(target, number_set)
        self.assertCountEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()
