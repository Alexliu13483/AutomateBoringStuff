'''
mcb.pyw
SPEC:
The program will save each piece of clipboard text under a keyword.
For example, when you run "py mcb.pyw save spam", the current contents of
the clipboard will be saved with the keyword spam. This text can later 
be loaded to the clipboard again by running "py mcb.pyw spam". And if 
the user forgets what keywords they have, they can run "py mcb.pyw list"
to copy a list of all keywords to the clipboard.

* The command line argument for the keyword is checked.
* If the argument is save, then the clipboard contents are saved to the keyword.
* If the argument is list, then all the keywords are copied to the clipboard.
* Otherwise, the text for the keyword is copied to the clipboard.

Usage:
py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
py.exe mcb.pyw list - Loads all keywords to clipboard.

Created on 2018-01-17

@author: Alex.Liu
'''
import shelve, pyperclip, sys

shelvefilename = r'.\data\mcb'
mcbShelf = shelve.open(shelvefilename)

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 1:
    print('he program will save each piece of clipboard text under a keyword.\n Command Format: mcb [save|list] <keyword>')


mcbShelf.close()

if __name__ == '__main__':
    pass