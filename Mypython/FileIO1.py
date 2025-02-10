'''
f = open('File.txt', 'w')
f.write("Eshwar\n")       # The data present in the file of the previous execution will be deleted
f.write(" Expert\n")      # For a single string
f.write(" in python\n")
l = ['Sunny\n', 'Bunny\n', 'Chinny\n', 'Vinny\n']
f.writelines(l)             # For all the strings in the list/tuple/set l
f.close()
print("File write operation completed")

f = open('File.txt', 'a')
f.write("Eshwar\n")       # The data present in the file will be appended with the previous file execution data
f.write("Expert\n")
f.write("in Java\n")
f.close()
print("File write operation completed")
'''

########################
#
# '''Problem: Write some data to a file, file name will be passed as dynamic input, data can be entered as dynamic input. The file must be created in a specific folder'''
# fname = input("Enter the name of the file:")
# f = open('/Users/eskumar/MyProject/Mypractice/'+fname, 'w')
# feedback = input('Enter your feedback:')
# f.writelines(feedback)
# f.close()

################################################################################################
# f = open('File.txt', 'r')
# # data1 = f.read() #To read total data
# # print(data1)
# # data2 = f.read(10)    # To read n characters from the file
# # print(data2)
# # data3 = f.readline()  # To read only one line
# # print(data3)
# # data4 = f.readlines() # to read all the lines and put it into a list
# # print(data4)
# data5 = f.readlines()
# for i in data5:
#     print(i)

# ################################################################################################
# '''Tell() method'''
# f = open('f2.txt')
# print(f.tell())
# print(f.read(2)) #Cursor will stay at the second position
# print(f.tell())
# print(f.readline())     # Cursor will read from the 3rd position complete line
# print(f.read(4))
# print('Remaining data')
# print(f.read())
# print(f.tell())

################################################################################################
# '''Problem: Read data from input.txt and write it to output.txt file'''
# f1 = open('input.txt', 'r')
# f2 = open('output.txt', 'w')
# f2.write(f1.read())
# f1.close()
# f2.close()
# print('Data from input.txt has been copied to output.txt')

################################################################################################
# '''With() Method in FileIO'''
# with open('python1', 'w') as f:
#     f.write("Eshwar\n")
#     f.write("Expert\n")
#     f.write("in python\n")
#     print("Is f closed?", f.closed)
# print("Is f closed?", f.closed)

# ################################################################################################
# '''Seek() method and r+ example'''
# data = "All students are Stupids" #S in stupids is at index 18 but the cursor starts from 0. So, cursor point will be 17
# f = open('abc1.txt', 'w')
# f.write(data)
# with open('abc1.txt', 'r+') as f:  #read and write
#     text = f.read()
#     print(text)
#     print("The current position:", f.tell())   #cursor goes to the last position after reading the complete string
#     f.seek(17)
#     print("The current position:", f.tell())    #cursor goes to 17th position
#     f.write("GEMS!!!")  #r+ means read and write, read the stupid( 7 characters) and replace it with "GEMS!!!"(7 characters)
#     f.seek(0)
#     text = f.read()
#     print("Data after modification")
#     print(text)

# ################################################################################################
# import os
# fname = input("Enter the name of the file:")
# if os.path.isfile(fname):
#     print("File exists:", fname)
#     f = open(fname, 'r')
#     print('The content of the file is:')
#     print(f.read())
# else:
#     print("The specified file does not exist")

################################################################################################
'''Problem: Find the number of lines, characters and words in a file.
File contains
All students are GEMS!!!      #here \n is also a character and the count increases by one for the first four lines but will not for the last line
All students are GEMS!!!
All students are GEMS!!!
All students are GEMS!!!
All students are GEMS!!!'''
'''Number of line: 5
   Number of words:20
   Number of characters:124'''

import os
fname = input("Enter the name of the file:")
if os.path.isfile(fname):
    print("File exists:", fname)
    f = open(fname, 'r')
    lcount = wcount = ccount = 0
    for line in f:
        lcount = lcount + 1
        words = line.split()
        wcount = wcount + len(words)
        ccount = ccount + len(line)
    print("The number of lines:",lcount)
    print("The number of words:", wcount)
    print("The Number of characters:", ccount)
else:
    print("The specified file does not exist")
