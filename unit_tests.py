#!/usr/bin/python3
import unittest
from random import randint
from all_sorts import Bubble, Shaker, Select, Merge, Quick, mQuick, Count, Counter

#=======================================================================================#
#===================================== Bubble Sort =====================================#
#=======================================================================================#

class TestBubbleSort(unittest.TestCase):
    test_name = 'Bubble Sort'

    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Bubble(randomList, c)
        try:
            self.assertEqual(c.mC, 45)
            self.assertEqual(c.mS, 13)
            self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])
        except Exception:
            log_failure(self.test_name, 1)
        
    def test_2_empty_list(self):
        c = Counter()
        Bubble([], c)
        try:
            self.assertEqual(c.mC, 0)
            self.assertEqual(c.mS, 0)
            self.assertEqual([], [])
        except Exception:
            log_failure(self.test_name, 2)

    def test_3_non_list(self):
        try:
            self.assertRaises(TypeError, Bubble, "string", Counter())
            self.assertRaises(TypeError, Bubble, 64, Counter())
            self.assertRaises(TypeError, Bubble, False, Counter())
        except Exception:
            log_failure(self.test_name, 3)

    # def test_4_random_large_list(self):
    #     randomList = []
    #     for i in range(2 ** 10):
    #         randomList.append(randint(0,1000))
        
    #     c = Counter()
    #     pySort = sorted(randomList[::])
    #     Bubble(randomList, c)
    #     self.assertEqual(randomList, pySort)

    # could be a good edge case to break (swapping numbers that are equal)??
    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        Bubble(randomList, c)
        try:
            self.assertEqual(c.mS, 0)
            self.assertEqual(c.mC, len(randomList) - 1)
            self.assertEqual(randomList, [0] * 20)
        except Exception:
            log_failure(self.test_name, 5)

    def test_6_returns_none(self):
        ret = Bubble([], Counter())
        try:
            self.assertIsNone(ret)
        except Exception:
            log_failure(self.test_name, 6)

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
        c = Counter()
        Shaker([], c)
        self.assertEqual(c.mC, 0)
        self.assertEqual(c.mS, 0)
        self.assertEqual([], [])

    def test_3_non_list(self):
        self.assertRaises(TypeError, Shaker, "string", Counter())
        self.assertRaises(TypeError, Shaker, 64, Counter())
        self.assertRaises(TypeError, Shaker, False, Counter())

    # def test_4_random_large_list(self):
    #     randomList = []
    #     for i in range(2 ** 10):
    #         randomList.append(randint(0,1000))
        
    #     c = Counter()
    #     pySort = sorted(randomList[::])
    #     Shaker(randomList, c)
    #     self.assertEqual(randomList, pySort)

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
    
    def test_2_empty_list(self):
        c = Counter()
        Select([], c)
        self.assertEqual(c.mC, 0)
        self.assertEqual(c.mS, 0)
        self.assertEqual([], [])

    def test_3_non_list(self):
        self.assertRaises(TypeError, Select, "string", Counter())
        self.assertRaises(TypeError, Select, 64, Counter())
        self.assertRaises(TypeError, Select, False, Counter())

    # def test_4_random_large_list(self):
    #     randomList = []
    #     for i in range(2 ** 10):
    #         randomList.append(randint(0,1000))
        
    #     c = Counter()
    #     pySort = sorted(randomList[::])
    #     Select(randomList, c)
    #     self.assertEqual(randomList, pySort)

    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        Select(randomList, c)
        self.assertEqual(c.mS, len(randomList))
        self.assertEqual(c.mC, 210)
        self.assertEqual(randomList, [0] * 20)

    def test_6_returns_none(self):
        ret = Select([], Counter())
        self.assertIsNone(ret)

#=======================================================================================#
#===================================== Merge Sort ======================================#
#=======================================================================================#

class TestMergeSort(unittest.TestCase):
    test_name = 'Merge Sort'

    def test_1_expected_use(self):
        randomList = [1,5,7,2,0,1,6,2,7,9]
        c = Counter()
        Merge(randomList, c)
        self.assertEqual(c.mC, 34)
        self.assertEqual(c.mS, 68)
        self.assertEqual(randomList, [0,1,1,2,2,5,6,7,7,9])

    def test_2_empty_list(self):
        c = Counter()
        Merge([], c)
        try:
            self.assertEqual(c.mC, 0)
            self.assertEqual(c.mS, 0)
            self.assertEqual([], [])
        except Exception:
            log_failure(self.test_name, 2)

    def test_3_non_list(self):
        try:
            self.assertRaises(TypeError, Merge, "string", Counter())
            self.assertRaises(TypeError, Merge, 64, Counter())
            self.assertRaises(TypeError, Merge, False, Counter())
        except Exception:
            log_failure(self.test_name, 3)

    # def test_4_random_large_list(self):
    #     randomList = []
    #     for i in range(2 ** 10):
    #         randomList.append(randint(0,1000))
        
    #     c = Counter()
    #     pySort = sorted(randomList[::])
    #     Merge(randomList, c)
    #     self.assertEqual(randomList, pySort)

    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        Merge(randomList, c)
        try:
            self.assertEqual(c.mS, 176)
            self.assertEqual(c.mC, 88)
            self.assertEqual(randomList, [0] * 20)
        except Exception:
            log_failure(self.test_name, 5)

    def test_6_returns_none(self):
        ret = Merge([], Counter())
        try:
            self.assertIsNone(ret)
        except Exception:
            log_failure(self.test_name, 6)

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

    def test_2_empty_list(self):
        c = Counter()
        Quick([], c)
        self.assertEqual(c.mC, 0)
        self.assertEqual(c.mS, 0)
        self.assertEqual([], [])

    def test_3_non_list(self):
        self.assertRaises(TypeError, Quick, "string", Counter())
        self.assertRaises(TypeError, Quick, 64, Counter())
        self.assertRaises(TypeError, Quick, False, Counter())

    # def test_4_random_large_list(self):
    #     randomList = []
    #     for i in range(2 ** 10):
    #         randomList.append(randint(0,1000))
        
    #     c = Counter()
    #     pySort = sorted(randomList[::])
    #     Quick(randomList, c)
    #     self.assertEqual(randomList, pySort)

    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        Quick(randomList, c)
        self.assertEqual(c.mS, 19)
        self.assertEqual(c.mC, 190)
        self.assertEqual(randomList, [0] * 20)

    def test_6_returns_none(self):
        ret = Quick([], Counter())
        self.assertIsNone(ret)

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

    def test_2_empty_list(self):
        c = Counter()
        mQuick([], c)
        self.assertEqual(c.mC, 0)
        self.assertEqual(c.mS, 0)
        self.assertEqual([], [])

    def test_3_non_list(self):
        self.assertRaises(TypeError, mQuick, "string", Counter())
        self.assertRaises(TypeError, mQuick, 64, Counter())
        self.assertRaises(TypeError, mQuick, False, Counter())

    # def test_4_random_large_list(self):
    #     randomList = []
    #     for i in range(2 ** 10):
    #         randomList.append(randint(0,1000))
        
    #     c = Counter()
    #     pySort = sorted(randomList[::])
    #     mQuick(randomList, c)
    #     self.assertEqual(randomList, pySort)

    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        mQuick(randomList, c)
        self.assertEqual(c.mS, 38)
        self.assertEqual(c.mC, 190)
        self.assertEqual(randomList, [0] * 20)

    def test_6_returns_none(self):
        ret = mQuick([], Counter())
        self.assertIsNone(ret)

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

    def test_2_empty_list(self):
        c = Counter()
        Count([], c)
        self.assertEqual(c.mC, 0)
        self.assertEqual(c.mS, 0)
        self.assertEqual([], [])

    def test_3_non_list(self):
        self.assertRaises(TypeError, Count, "string", Counter())
        self.assertRaises(TypeError, Count, 64, Counter())
        self.assertRaises(TypeError, Count, False, Counter())

    # def test_4_random_large_list(self):
    #     randomList = []
    #     for i in range(2 ** 10):
    #         randomList.append(randint(0,1000))
        
    #     c = Counter()
    #     pySort = sorted(randomList[::])
    #     Count(randomList, c)
    #     self.assertEqual(randomList, pySort)

    def test_5_dup_list(self):
        randomList = [0] * 20
        c = Counter()
        Count(randomList, c)
        self.assertEqual(c.mS, 20)
        self.assertEqual(c.mC, 20)
        self.assertEqual(randomList, [0] * 20)

    def test_6_returns_none(self):
        ret = Count([], Counter())
        self.assertIsNone(ret)

def main(defaultTest=None):
    unittest.main(defaultTest=defaultTest, exit=False)
    
def log_failure(test_class, test_number):
    fout = open("failures.txt", "a")
    fout.write("{:<15} | {:<10}\n".format(test_class, test_number))
    fout.close()

if __name__ == '__main__':
    main()
