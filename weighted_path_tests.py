#!/usr/bin/python3
import unittest
from random import randint
from weighted_path import WeightedPath

#=======================================================================================#
#==================================== Weighted Path ====================================#
#=======================================================================================#

class TestWeightedPath(unittest.TestCase):
    def test_1_expected_use(self):
        nodes = [node for node in range(10)]
        wp = WeightedPath(nodes, startingWeight=1.0, positiveWeight=.01, negativeWeight=.99)
        for i in range(5):
            wp.PositivePass(i)
        wp.NegativePass(0)
        for i in range(5, 10):
            wp.NegativePass(i)
        
        # This is how negative[0, 5-9] and positive[0-4] would look. Is this what we want?
        self.assertEqual(wp.GetPaths(), {
            0: .0099,
            1: .01,
            2: .01,
            3: .01,
            4: .01,
            5: .99,
            6: .99,
            7: .99,
            8: .99,
            9: .99,
        })


        

if __name__ == '__main__':
    unittest.main()