import os
#Write a Python program to list only directories, files and all directories, files in a specified path.
def fd(path):
    l=os.listdir(path)
    files=[]
    dirs=[]
    for i in l:
        if(os.path.isfile(i)):
            files.append(i)
        else:
            dirs.append(i)
    print(files)
    print(dirs)
#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def check(path):
           path1 = os.access(path, os.F_OK)
           print("Does the path exists:", path1)
           path2 = os.access(path, os.R_OK)
           print("Access to read the file:", path2)
           path3 = os.access(path, os.W_OK)
           print("Access to write to file:", path3)
           path4 = os.access(path, os.X_OK)
           print("Can path be executed:", path4)
#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

def portion(path):
           if(os.path.exists(path1)):
               print(os.path.basename(path))
               print(os.path.abspath(path))
           else:
               print("Incorrect directory")
portion("./dir.py")
#Write a Python program to count the number of lines in a text file.
def count(path):
    f = open(path, "r", encoding="utf-8")
    s=int(0)
    for x in f:
      s=s+1
    print(s)
    f.close()
path="row.txt"
count(path)
#Write a Python program to write a list to a file.
def writelist(l):
    f = open("newfile.txt", "a", encoding="utf-8")
    for i in l:
        f.write(l)
    f.close()
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def create():
    for i in range(0,26):
        open(chr(65+i)+".txt","x",encoding="utf-8")
#Write a Python program to copy the contents of a file to another file
def copy(path1,path2):
    f=open(path1,"r",encoding="utf-8")
    f2=open(path2,"a",encoding="utf-8")
    for i in f:
        f2.write(i)
    f.close()
    f2.close()
copy("row.txt","row2.txt")
#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def del(path):
    if os.path.exists(path):
      os.remove(path)

    
    
           
