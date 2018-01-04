'''
Created on 2018-01-03

@author: Alex.Liu
'''

import os

def getTotalSize(path = '.'):
    totalSize = 0
    for filename in os.listdir(path):
        if os.path.isdir(path + '\\' + filename) == True:
            totalSize += getTotalSize(os.path.join(path, filename))
        else:
            totalSize += os.path.getsize(os.path.join(path, filename))
    return totalSize

if __name__ == '__main__':
    pass