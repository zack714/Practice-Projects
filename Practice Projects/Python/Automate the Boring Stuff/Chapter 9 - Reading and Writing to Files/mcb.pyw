#! python3
# mcb.pyw - Saves and loads parts of text to the cipboard
#Usage: py.exe mcb.pyw save <keyword> - Loads keyword to clipbaord.
#       py.exe mcb.pyw <keyword> - loads keyword to clipboard
#       py.exe mcb.pyw list - Loads all keywords to clipboard
#       py.exe mcb.pyw delete <keyword> - Deletes keyword and its associated text
#       py.exe mcb.pyw delete - Deletes all keywords and their associated strings of text
#argv = "argument vector" - list of strings that represent the input passed to the cmd line

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del[sys.argv[2]]
        print(f"Keyword {sys.argv[2]} and its corresponding text deleted from shelf.")

elif len(sys.argv)==2:

#TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print("All keywords and their corresponding text deleted.")
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.copy[1]])

mcbShelf.close()