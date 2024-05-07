import unittest
from add import add, add_many, add_numalpha
from sub import sub


class Calc_Test(unittest.TestCase):

    
    def test_add(self):
        self.assertEqual(9, add(5,4))


    @unittest.skip("NA for now")   
    def test_add_only_numbers(self):
        with self.assertRaises(TypeError):
            add(5, str(5))


     
    def test_add_many(self):
        self.assertEqual(10, add_many(1,2,3,4))


    def test_sub(self):
        self.assertEqual(1, sub(5,4))


    #@unittest.skip("WIP")
    def test_add_num_and_words(self):
        self.assertTrue("5a" == add_numalpha(5, "a"))

