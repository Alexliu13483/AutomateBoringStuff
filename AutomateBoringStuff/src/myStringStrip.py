'''
Created on 2017-12-28

@author: Alex.Liu
'''
import re

def strip(inString, rev=r'\s'):
    if rev == r'\s':
        patStrip = rev + r'*(.*\S)?' + rev + r'*$'
        regexStrip = re.compile(patStrip)
        m = regexStrip.search(inString)
    else:
        patStrip = r'[' + rev + r']*([^' + rev + r'].*[^' + rev + r'])?[' + rev + r']*$'
        regexStrip = re.compile(patStrip)
        m = regexStrip.search(inString)
        
    if m != None:
        return m.group(1)
    return ''

if __name__ == '__main__':
    pass