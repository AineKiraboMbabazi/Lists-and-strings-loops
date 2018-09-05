from fizzbuzz import fizzbuzz
import unittest

class testfizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        #assertMultiLineEqual() used when comparing two strings
        self.assertMultiLineEqual(fizzbuzz([1,2,3],[]),'fizz')
        self.assertMultiLineEqual(fizzbuzz([4],[1,2,3,4]),'buzz')
        self.assertMultiLineEqual(fizzbuzz([1,1,2,3,5,6,7,8,9,0],[1,2,3,4,5]),'fizzbuzz')
        self.assertEqual(fizzbuzz([1,2,3,4],[]),4)

    def test_input_lists(self):
        self.assertEqual(fizzbuzz((1,3,4),()),'please enter lists only')
        
if __name__ == '__main__':
    unittest.main()
    