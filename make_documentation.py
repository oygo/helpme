import os
import shutil

# set the current directory to the where the code snippets are
jekyll_abs = os.getcwd()
notes_rel = '../../Notes/Code Snippets/'
notes_abs = os.path.join(os.getcwd(), notes_rel)
os.chdir(notes_abs)

print(os.listdir()) # returns list

file = 'Functions  - Lambda expressions.md'

shutil.copy2('Functions  - Lambda expressions.md', jekyll_abs) # target filename is /dst/dir/file.ext

# os. 'Functions  - Lambda expressions.md'