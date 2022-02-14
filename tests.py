import unittest
from check_pwd import check_pwd


class TestClass(unittest.TestCase):
    # checks if the input is empty, should return false
    def test1(self):
        pw = ''
        expected = False
        self.assertEqual(check_pwd(pw), expected)

    # pw meets all the criteria
    def test2(self):
        pw = 'ABCde12!@'
        expected = True
        self.assertEqual(check_pwd(pw), expected)

    # string less than 8 characters
    def test3(self):
        pw = 'ABCd12!'
        expected = False
        self.assertEqual(check_pwd(pw), expected)

    # string more than 20 characters
    def test4(self):
        pw = 'ABCabc123123ABCabc123123!#!@'
        expected = False
        self.assertEqual(check_pwd(pw), expected)

    # String with no lowercase letter
    def test5(self):
        pw = 'ABCD123@#'
        expected = False
        self.assertEqual(check_pwd(pw), expected)

    # string with no uppercase
    def test6(self):
        pw = 'abcd123@#'
        expected = False
        self.assertEqual(check_pwd(pw), expected)

    # string with no digits
    def test7(self):
        pw = 'ABCdef!@'
        expected = False
        self.assertEqual(check_pwd(pw), expected)

    # string with no symbols
    def test8(self):
        pw = 'ABCdef123'
        expected = False
        self.assertEqual(check_pwd(pw), expected)


if __name__ == '__main__':
    unittest.main()
