#!/usr/bin/python3
import unittest
from random import randint
from all_sorts import Bubble, Shaker, Select, Merge, Quick, mQuick, Count, Counter

#=======================================================================================#
#===================================== Bubble Sort =====================================#
#=======================================================================================#

class TestBubbleSort(unittest.TestCase):
    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Bubble(randomList, c)
        self.assertEqual(c.mC, 45)
        self.assertEqual(c.mS, 13)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])
        
    def test_2_empty_list(self):
        randomList = []
        c = Counter()
        Bubble(randomList, c)
        self.assertEqual(c.mC, 0)
        self.assertEqual(c.mS, 0)
        self.assertEqual(randomList, [])

    def test_3_non_list(self):
        self.assertRaises(TypeError, Bubble, "string", Counter())
        self.assertRaises(TypeError, Bubble, 64, Counter())
        self.assertRaises(TypeError, Bubble, False, Counter())

    def test_4_random_large_list(self):
        randomList = []
        for i in range(2 ** 10):
            randomList.append(randint(0,1000))
        
        c = Counter()
        pySort = sorted(randomList[::])
        Bubble(randomList, c)
        self.assertEqual(randomList, pySort)

    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        Bubble(randomList, c)
        self.assertEqual(c.mS, 0)
        self.assertEqual(c.mC, len(randomList) - 1)
        self.assertEqual(randomList, [0] * 20)

    def test_6_returns_none(self):
        ret = Bubble([], Counter())
        self.assertIsNone(ret)

#=======================================================================================#
#===================================== Shaker Sort =====================================#
#=======================================================================================#

class TestShakerSort(unittest.TestCase):
    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Shaker(randomList, c)
        self.assertEqual(c.mC, 54)
        self.assertEqual(c.mS, 13)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])
        
    def test_2_empty_list(self):
        randomList = []
        c = Counter()
        Shaker(randomList, c)
        self.assertEqual(c.mC, 0)
        self.assertEqual(c.mS, 0)
        self.assertEqual(randomList, [])

    def test_3_non_list(self):
        self.assertRaises(TypeError, Shaker, "string", Counter())
        self.assertRaises(TypeError, Shaker, 64, Counter())
        self.assertRaises(TypeError, Shaker, False, Counter())

    def test_4_random_large_list(self):
        randomList = []
        for i in range(2 ** 10):
            randomList.append(randint(0,1000))
        
        c = Counter()
        pySort = sorted(randomList[::])
        Shaker(randomList, c)
        self.assertEqual(randomList, pySort)

    # could be a good edge case to break??
    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        Shaker(randomList, c)
        self.assertEqual(c.mS, 0)
        self.assertEqual(c.mC, (len(randomList) * 2) - 2)
        self.assertEqual(randomList, [0] * 20)

    def test_6_returns_none(self):
        ret = Shaker([], Counter())
        self.assertIsNone(ret)
        
#=======================================================================================#
#===================================== Select Sort =====================================#
#=======================================================================================#

class TestSelectSort(unittest.TestCase):
    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Select(randomList, c)
        self.assertEqual(c.mC, 55)
        self.assertEqual(c.mS, 10)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])

#=======================================================================================#
#===================================== Merge Sort ======================================#
#=======================================================================================#

class TestMergeSort(unittest.TestCase):
    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Merge(randomList, c)
        self.assertEqual(c.mC, 34)
        self.assertEqual(c.mS, 68)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])

#=======================================================================================#
#===================================== Quick Sort ======================================#
#=======================================================================================#

class TestQuickSort(unittest.TestCase):
    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Quick(randomList, c)
        self.assertEqual(c.mC, 23)
        self.assertEqual(c.mS, 13)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])

#=======================================================================================#
#===================================== mQuick Sort =====================================#
#=======================================================================================#

class TestmQuickSort(unittest.TestCase):
    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        mQuick(randomList, c)
        self.assertEqual(c.mC, 30)
        self.assertEqual(c.mS, 17)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])

#=======================================================================================#
#===================================== Count Sort ======================================#
#=======================================================================================#

class TestCountSort(unittest.TestCase):
    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Count(randomList, c)
        self.assertEqual(c.mC, 10)
        self.assertEqual(c.mS, 10)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])

if __name__ == '__main__':
    unittest.main()