'''
Created on 2017-12-28

@author: Alex.Liu
'''
import unittest
import passwordDetection


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testLessThanEight(self):
        msg = 'Password length is less than 8'
        testPassword = 'abcEEE'
        expect = False
        actual = passwordDetection.check(testPassword)
        self.assertEqual(expect, actual, msg)

    def testOnlyCapital(self):
        msg = 'Password does not have lowercase char'
        testPassword = 'ABCDEFG123'
        expect = False
        actual = passwordDetection.check(testPassword)
        self.assertEqual(expect, actual, msg)

    def testOnlyLowercaseChars(self):
        msg = 'Password does not have uppercase char'
        testPassword = 'abcdefg123'
        expect = False
        actual = passwordDetection.check(testPassword)
        self.assertEqual(expect, actual, msg)

    def testNoUpperAndLowercaseChars(self):
        msg = 'Password does not have uppercase or lowercase char'
        testPassword = '123123123'
        expect = False
        actual = passwordDetection.check(testPassword)
        self.assertEqual(expect, actual, msg)

    def testNoDigitChars(self):
        msg = 'Password does not have digit char'
        testPassword = 'ABCdefghijk'
        expect = False
        actual = passwordDetection.check(testPassword)
        self.assertEqual(expect, actual, msg)

    def testCorrectPassword(self):
        msg = 'Password format is correct'
        testPassword = 'ABCdefghi123'
        expect = True
        actual = passwordDetection.check(testPassword)
        self.assertEqual(expect, actual, msg)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()