import unittest
from a import app
class MTestCase(unittest.TestCase):
    def test_1(self):
        app.testing = True
        response = app.test_client().get('/')
        source = response.data.decode('UTF-8')
        self.assertEqual(response.status_code,200)
    def test_2(self):
        app.testing = True
        response = app.test_client().post('/add',data={'a':1,'b':2})
        data = response.data.decode('UTF-8')
        self.assertEqual(data,'3')
if __name__ == '__main__':
    unittest.main()