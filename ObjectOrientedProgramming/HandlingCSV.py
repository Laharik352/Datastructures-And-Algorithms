# '''Probelm: Write data to a CSV file'''
# import csv
# with open("student.csv", 'w') as f:
#     w = csv.writer(f)       #CSV wirter object can be got by using writer()
#     w.writerow(['NAME','ROLLNO','MARKS','ADDR'])    #writerow is the method provided by the csv module
#     while True:
#         name = input("Enter the name of the student:")
#         rollno = input("Enter the rollno of the student:")
#         marks = input("Enter the marks of the student:")
#         addr = input("Enter the address of the student:")
#         w.writerow([name, rollno, marks,addr] )
#         option = input("Do you want to enter next student details [YES|NO]")
#         if option.lower() == "no":
#             break
# print("Data has been added to the file successfully")

'''Problem: Read the data from a csv file'''
import csv
f = open('student.csv','r')
r = csv.reader(f)
data = list(r)
print(data)