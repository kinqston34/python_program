import unittest
def add(a,b):
    return a+b
# object oriented programming
class MTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(1,1),2)
    def test_2(self):
        self.assertEqual(add(1,1),1)

if __name__ == '__main__':
    unittest.main()