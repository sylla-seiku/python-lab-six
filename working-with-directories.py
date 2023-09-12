#Learning about working with directories 
from pathlib import Path

path = Path("emails")
print(path.exists()) #this checks to see if a directory exists

#path = Path("ecommerce")
#print(path.mkdir()) # this makes a directory

#path = Path("ecommerce")
#print(path.rmdir()) # this action removes the directory.


path = Path()
for file in path.glob('*.py'): #this gives me all the "py" files in this directory.
    print(file)



path = Path()
for file in path.glob('*'): #this prints everything in the directories.
    print(file)

