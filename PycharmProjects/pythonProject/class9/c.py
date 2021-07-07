import unittest
def check_id(id):
    if len(id) != 10:
        return False
    #第一碼: 大寫英文
    if not id[0].isupper():
        return False
    #第二碼 : 1,2
    if not id[1] in '12':
        return False
    for x in id[2:]:
        if not x.isdigit():
            return False
    return True
class MTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_id('A12345896'),False)     #長度不足10碼
    def test_2(self):
        self.assertEqual(check_id('a123456789'),False)    #大寫不是英文
    def test_3(self):
        self.assertEqual(check_id('A345678900'),False)    #第二碼不是1,2
    def test_4(self):
        self.assertEqual(check_id('A14a++4568'),False)    #第二碼後不是數字
    def test_5(self):
        self.assertEqual(check_id('Q111245789'),True)    #正確版本

if __name__ == '__main__':
    unittest.main()