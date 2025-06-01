import unittest
from .solution import solution

class TestSolution(unittest.TestCase):
    def test(self):
        str1 = "abcdef"
        str2 = "azced"
        expected = 3
        observed = solution(str1, str2)
        self.assertEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()
