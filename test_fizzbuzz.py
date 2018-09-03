from fizzbuzz import fizzbuzz
import unittest

class testfizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        a=[1,2,3]
        b=[]
        c=[4]
        d=[1,1,2,3,5,6,7,8,9,0]
        e=[1,2,3,4]
        f=[1,2,3,4,5]
        fizzbuzz(a,b)
        fizzbuzz(c,e)
        fizzbuzz(d,f)
        fizzbuzz(e,b)
        self.assertEqual(fizzbuzz(a,b),'fizz')
        self.assertEqual(fizzbuzz(c,e),'buzz')
        self.assertEqual(fizzbuzz(d,f),'fizzbuzz')
        self.assertEqual(fizzbuzz(e,b),4)


if __name__ == '__main__':
    unittest.main()
    