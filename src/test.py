import unittest

from functions.converter import converter

from functions.greedy import Min_Matching_Greedy
from functions.recursive import Min_Matching_Recursive
from functions.memorized import Min_Matching_Memorized, CleanMemoria


class MinMatchProblems(unittest.TestCase):
    def test_converter(self):
        query = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
        expect = [3, 1, 2, 2, 3, 1]
        self.assertEqual(converter(query), expect)

    def test_greedy(self):
        query1 = [3, 1, 2, 2, 3, 1]
        query2 = [2, 2, 5, 2]
        expectMatch = [(3, [2, 2]), ([1, 2], 5), ([2, 3, 1], 2)]
        expectPeso = 4.35
        self.assertEqual(Min_Matching_Greedy(query1, query2)[0], expectMatch)
        self.assertEqual(Min_Matching_Greedy(query1, query2)[1], expectPeso)

    def test_recursive(self):
        query1 = [1, 2, 3, 2, 1]
        query2 = [3, 2, 1, 2, 3]
        expect = [([1, 2], 3), (3, [2, 1, 2]), ([2, 1], 3)]
        self.assertEqual(Min_Matching_Recursive(query1, query2), expect)
        query1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        query2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expect = [([1, 2, 3, 4, 5, 6, 7, 8], 10), (9, [9, 8, 7]), (10, [6, 5, 4, 3, 2, 1])]
        self.assertEqual(Min_Matching_Recursive(query1, query2), expect)

    def test_memorized(self):
        query1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        query2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expect = [([1, 2, 3, 4, 5, 6, 7, 8], 10), (9, [9, 8, 7]), (10, [6, 5, 4, 3, 2, 1])]
        self.assertEqual(Min_Matching_Memorized(query1, query2), expect)
        CleanMemoria()
        query1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        query2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expect = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 20), (17, [19, 18, 17]), (18, [16, 15, 14]),
                  (19, [13, 12, 11, 10]), (20, [9, 8, 7, 6, 5, 4, 3, 2, 1])]
        self.assertEqual(Min_Matching_Memorized(query1, query2), expect)


if __name__ == '__main__':
    unittest.main()
