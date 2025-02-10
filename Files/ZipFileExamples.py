'''Zip file creation'''
# from zipfile import *
# f = ZipFile('files.zip', 'w', ZIP_DEFLATED)
# f.write('abc.txt')
# f.write('abc1.txt')
# f.close()
# print("Zip file created successfully")
######################################################################################
'''Unzipping and reading the contents of the zip file'''
from zipfile import *
f = ZipFile('files.zip', 'r', ZIP_STORED)
names = f.namelist()
for file in names:
    print("Name of file", file)
    print("The content of the file is:")
    f1=open(file, 'r')
    print(f1.read())
    print("*"*10)