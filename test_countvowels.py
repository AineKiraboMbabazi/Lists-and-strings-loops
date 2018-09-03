from countvowels import vowel_count
import unittest
class testcountvowels(unittest.TestCase):
    def test_countvowels(self):
        self.assertEqual(vowel_count('hellothere'),('eo', 4))






if __name__ == '__main__':
    unittest.main()