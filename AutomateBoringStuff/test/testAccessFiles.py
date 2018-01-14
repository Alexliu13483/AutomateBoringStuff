'''
Created on 2018-01-03

@author: Alex.Liu
'''
import unittest
import automationFileSystem


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_totalSizeOfFiles_withoutSub(self):
        testPath = r'.\testdata\testfor_getTotalSize\subfolder'
        expect = 55026
        result = automationFileSystem.getTotalSize(testPath)
        self.assertEqual(expect, result, 'test_totalSizeOfFiles_withoutSub')

    def test_totalSizeOfFiles_withSub(self):
        testPath = r'.\testdata\testfor_getTotalSize'
        expect = 226201
        result = automationFileSystem.getTotalSize(testPath)
        self.assertEqual(expect, result, 'test_totalSizeOfFiles_withSub')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_totalSizeOfFiles']
    unittest.main()