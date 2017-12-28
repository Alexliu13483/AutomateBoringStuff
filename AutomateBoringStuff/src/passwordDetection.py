'''
Created on 2017-12-28

@author: Alex.Liu

Write a function that uses regular expressions to make sure the password string
it is passed is strong. A strong password is defined as one that is 
1. at least eight characters long, 
2. contains both uppercase and lowercase characters, 
3. and has at least one digit. 
You may need to test the string against multiple regex patterns to validate 
its strength.
'''

import re

regex1 = re.compile(r'\w{8,}')
regex2 = re.compile(r'\w*[a-z]+\w*')
regex3 = re.compile(r'\w*[A-Z]+\w*')
regex4 = re.compile(r'\w*[0-9]+\w*')

def check(password):
    m = regex1.match(password)
    if m == None:
        return False
    elif regex2.match(password) == None:
        return False
    elif regex3.match(password) == None:
        return False
    elif regex4.match(password) == None:
        return False
    
    return True

if __name__ == '__main__':
    pass