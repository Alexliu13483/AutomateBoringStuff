'''
Created on 2017-12-28

@author: Alex.Liu
'''
import unittest
import myStringStrip

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStingStripDefault1(self):
        msg = 'testStingStripDefault1'
        testString = '   Hello World!!!   '
        expect = 'Hello World!!!'
        actual = myStringStrip.strip(testString)
        self.assertEqual(expect, actual, msg)

    def testStingStripDefault2(self):
        msg = 'testStingStripDefault2'
        testString = '   Hello World!!! \t  \n'
        expect = 'Hello World!!!'
        actual = myStringStrip.strip(testString)
        self.assertEqual(expect, actual, msg)

    def testStingStripWithSpecificRev(self):
        msg = 'testStingStripDefault2'
        testString = '   Hello World!!! 123'
        expect = '   Hello World!!! '
        actual = myStringStrip.strip(testString, rev='123')
        self.assertEqual(expect, actual, msg)

    def testStingStripWithSpecificRev1(self):
        msg = 'testStingStripDefault2'
        testString = '   Hello World!!! 111'
        expect = '   Hello World!!! '
        actual = myStringStrip.strip(testString, rev='123')
        self.assertEqual(expect, actual, msg)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()