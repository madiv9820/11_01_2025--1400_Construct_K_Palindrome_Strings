from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ('annabelle', 2, True),
                            2: ('leetcode', 3, False),
                            3: ('true', 4, True)}
        self.__obj = Solution()
        return super().setUp()

    @timeout(0.5)
    def test_case_1(self):
        s, k, output = self.__testcases[1]
        result = self.__obj.canConstruct(s = s, k = k)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        s, k, output = self.__testcases[2]
        result = self.__obj.canConstruct(s = s, k = k)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        s, k, output = self.__testcases[3]
        result = self.__obj.canConstruct(s = s, k = k)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()