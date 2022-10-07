#!/usr/bin/python3
import unittest
from sorting_algorithms import Bubble, Shaker, Counts

class TestStringMethods(unittest.TestCase):

    def test_shaker_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        Shaker(randomList, Counts())
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])
        
    def test_shaker_2_empty_list(self):
        randomList = []
        Shaker(randomList, Counts())
        self.assertEqual(randomList, [])
        
    def test_bubble_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        Bubble(randomList, Counts())
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])

    def test_bubble_2_empty_list(self):
        randomList = []
        Bubble(randomList, Counts())
        self.assertEqual(randomList, [])

if __name__ == '__main__':
    unittest.main()