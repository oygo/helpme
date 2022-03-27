import os
import shutil

# set the current directory to the where the code snippets are
jekyll_abs = os.getcwd()
notes_rel = '../../Notes/Code Snippets/'
notes_abs = os.path.join(os.getcwd(), notes_rel)
os.chdir(notes_abs)

p = os.listdir() # returns list
p.remove('.obsidian')
for i in p:
    if os.path.isdir(i): # i is a directory
        print(f'directory name: {i}')
    else: # i is a file
        print(f'file name: {i}')


#print(contents)
# print(contents[0])

#file = 'Functions  - Lambda expressions.md'

#shutil.copy2('Functions  - Lambda expressions.md', jekyll_abs) # target filename is /dst/dir/file.ext

# os. 'Functions  - Lambda expressions.md'


