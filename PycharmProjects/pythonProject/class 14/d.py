import requests
import unittest
class MTestCase(unittest.TestCase):
    def test_1(self):
        r = requests.post('http://127.0.0.1:5000/add',data={'a':10,'b':20})
        self.assertEqual(r.text,'30')
if __name__ == '__main__':
    unittest.main()