import unittest
from RocketProgram import get_rockets_stats, is_negative

class TestRocketStats(unittest.TestCase):

    def test_input_data_value(self):
        self.assertRaises(ValueError, get_rockets_stats, ([-1,-2,-3], [-5,-8,-23], [1,-22, -23]))
    
    def test_input_data_type(self):
        self.assertRaises(TypeError, get_rockets_stats,  ([1,2,3], [5,8,23], [1,22, 23]))

    def test_is_negative(self):
        self.assertRaises(TypeError, is_negative, "blabla")
        self.assertRaises(TypeError, is_negative, 123)
        self.assertRaises(TypeError, is_negative, True)
        self.assertRaises(TypeError, is_negative, 1+35j)
        
if __name__ == '__main__':
    unittest.main()