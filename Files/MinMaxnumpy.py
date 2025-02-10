import numpy
n = int(input().split()[0])
ar = []
for i in range(n):
    mar = numpy.array(input().split(), int)
    ar.append(mar)
ar = numpy.array(ar)
# print(ar)
print(numpy.max(numpy.min(ar, axis = 1)))