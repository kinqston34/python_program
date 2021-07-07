#test c.py(use MVC: model view controller) #內部測試
import unittest
from c import app

class MTtestCase(unittest.TestCase):
    def test_1(self):
        app.testing = True
        response = app.test_client().get('/')
        #print(response.data,type(response.data))
        source = response.data.decode('UTF-8')
        #print(source,type(source))
        self.assertEqual(response.status_code,200)
    def test_2(self):
        app.testing = True
        response = app.test_client().post('/add',data={'a':1,'b':2})
        data = response.data.decode('UTF-8')
        self.assertEqual(data,"3")
if __name__ == '__main__':
    unittest.main()
