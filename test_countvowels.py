from countvowels import vowel_count
import unittest
class testcountvowels(unittest.TestCase):
    def test_countvowels(self):
        self.assertEqual(vowel_count('hello there'),(('a', 0), ('e', 3), ('i', 0), ('o', 1), ('u', 0)))






if __name__ == '__main__':
    unittest.main()