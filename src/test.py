import unittest

from functions.converter import converter

from functions.greedy import Min_Matching
import functions.recursive
import functions.memorized
import functions.dynamic_programming

class MinMatchProblems(unittest.TestCase):
    def test_converter(self):
        query = [0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0]
        expect = [3,1,2,2,3,1]
        self.assertEqual(converter(query), expect)

    def test_greedy(self):
        query1 = [3,1,2,2,3,1]
        query2 = [2,2,5,2]
        expect = [(3,[2, 2]),([1,2],5),([2,3,1],2)]
        self.assertEqual(Min_Matching(query1, query2), expect)
    
    def test_recursive(self):
        self.assertEqual(1, 1)
    
    def test_memorized(self):
        self.assertEqual(1, 1)
    
    def test_dynamic_programming(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()