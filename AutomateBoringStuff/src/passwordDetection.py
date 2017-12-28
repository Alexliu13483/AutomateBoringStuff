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

regexPassword = re.compile(r'''
                            ^
                            (?=.*[A-Z])
                            (?=.*[a-z])
                            (?=.*[0-9])
                            .{8,}
                            $
                            ''', re.VERBOSE)

def check(password):
    m = regexPassword.match(password)
    if m == None:
        return False
    return True

if __name__ == '__main__':
    pass