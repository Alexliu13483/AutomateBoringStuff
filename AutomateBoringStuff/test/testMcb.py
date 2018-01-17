'''
Created on 2018-01-17

@author: Alex.Liu
'''
import unittest
import pyperclip
import shelve
import importlib
import mcb
import sys

class Test(unittest.TestCase):


    def setUp(self):
        mcbShelf = shelve.open('mcb')
        mcbShelf.clear()
        mcbShelf.close()


    def tearDown(self):
        pass

    def prepareTwoData(self):
        expectData = ['one_Data', 'two_Data']
        expectKeys = ['one', 'two']
        pyperclip.copy(expectData[0])
        sys.argv = ['', 'save', expectKeys[0]]
        importlib.reload(mcb)
        pyperclip.copy(expectData[1])
        sys.argv = ['', 'save', expectKeys[1]]
        importlib.reload(mcb)
        return expectData, expectKeys


    def test_saveOnePicecOfData(self):
        expect = 'one_Data'
        pyperclip.copy(expect)
        sys.argv = ['', 'save', 'one']
        importlib.reload(mcb)
        mcbShelf = shelve.open('mcb')
        self.assertEqual(expect, mcbShelf['one'], 'saveOnePicecOfData')
        mcbShelf.close()
        

    def test_saveTwoPicecOfData(self):
        expectData, expectKeys = self.prepareTwoData()
        
        mcbShelf = shelve.open('mcb')
        self.assertEqual(expectData[0], mcbShelf[expectKeys[0]], 'test_saveTwoPicecOfData_0')
        self.assertEqual(expectData[1], mcbShelf[expectKeys[1]], 'test_saveTwoPicecOfData_1')
        mcbShelf.close()
        
    def test_listStoredData(self):
        _, expectKeys = self.prepareTwoData()
        expect = str(expectKeys)

        sys.argv = ['', 'list']
        importlib.reload(mcb)
        mcbShelf = shelve.open('mcb')
        self.assertEqual(expect, pyperclip.paste(), 'listStoredData')
        mcbShelf.close()

    def test_getStoredData(self):
        expectData, expectKeys = self.prepareTwoData()

        sys.argv = ['', expectKeys[0]]
        importlib.reload(mcb)
        mcbShelf = shelve.open('mcb')
        self.assertEqual(expectData[0], pyperclip.paste(), 'getStoredData')
        mcbShelf.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()