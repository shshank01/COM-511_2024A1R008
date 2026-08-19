# write a python program to print the content of a directory using the os module. Search online for the function which does that.
'''import os
files = os.listdir()
print(files)'''

# To print the path of the current working directory
'''import os
print(os.getcwd())'''

# To create a new folder in the current directory
'''import os
os.mkdir('demo')'''

# To check whether the folder exist or not
'''import os
print(os.path.exists('demo'))
print(os.path.exists('a1'))'''

# To rename the file or directory
'''import os
os.rename('2.py','rename.py')'''

# To check whether the argument is file or not
'''import os
print(os.path.isfile('3.py'))
print(os.path.isfile('p.py'))'''

# To check whether the argument is directory or not
'''import os
print(os.path.isdir('demo'))
print(os.path.isdir('hallelujah'))'''

# To remove a file from current directory
'''import os
os.remove('3.py')'''

# To remove a file from current directory
'''import os
os.rmdir('demo')'''

