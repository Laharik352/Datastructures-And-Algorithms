from sys import argv
args = argv[1:]
sum = 0
for i in args:
    sum+=int(i)
print("The sum:", sum) #python python1.py 10 20 30
print("The sum: {}".format(sum))
print("The sum: %i" %(sum))
t= (10, 20, 30, 40)
a,b,c,d = t
print(a)

