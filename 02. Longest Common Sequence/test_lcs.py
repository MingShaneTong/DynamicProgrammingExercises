import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test(self):
        str1 = "abcdaf"
        str2 = "acbcf"
        expected = "abcf"
        observed = solution(str1, str2)
        self.assertEqual(expected, observed)

if __name__ == "__main__":
    unittest.main()
