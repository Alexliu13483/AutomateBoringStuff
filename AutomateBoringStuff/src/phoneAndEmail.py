#! Python3
'''
Created on 2017-12-22
Automate the boring stuff exercise
Finds phone numbers and email addresses on the clipboard
@author: Alex.Liu
'''

import pyperclip, re

# Create Phone Number regex
phoneRegex = re.compile(r'''(
    (\d{1}|\+\d{3}|\.)?        # National code
    (\s|-|\.)                # separator
    (\d{3}|\(\d{3}\))?        # area code
    (\s|-|\.)                # separator
    (\d{3})                    # first 3 digits
    (\s|-|\.)                # separator
    (\d{4})                    # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.X)

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+            # username
    @                            # @ symbol
    [a-zA-Z0-9.-]+                # domain name
    (\.[a-zA-Z]{2,4})            # dot-something
    )''', re.X)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    if groups[8] != '':
        phoneNum += ' x' + groups[10]
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')

if __name__ == '__main__':
    pass