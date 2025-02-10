'''Normal Example without using threads'''
# import time
# def doubles(numbers):
#     for i in numbers:
#         time.sleep(1)
#         print("The double:", 2*i)
# def squares(numbers):
#     for j in numbers:
#         time.sleep(1)
#         print("The squares:", j*j)
# numbers = [1,2,3,4,5,6]
# begintime = time.time()
# doubles(numbers)
# squares(numbers)
# endtime = time.time()
# print("The time taken:", endtime - begintime)     #12.03742790222168

'''Same above example using threads'''
import time
from threading import *
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print("The double:", 2*i)
def squares(numbers):
    for j in numbers:
        time.sleep(1)
        print("The squares:", j*j)
numbers = [1,2,3,4,5,6]
begintime = time.time()
t1 = Thread(target=doubles, args=(numbers, ))     # The args must be provided in the form of tuple only
t2 = Thread(target=squares, args=(numbers, ))
t1.start()
t2.start()
t1.join()   # THis join() method required to ensure that main thread does not run until the t1 thread is completed
t2.join()   # This join() method required to ensure that main thread does not run until the t2 thread is completed
endtime = time.time()
print("The time taken:", endtime - begintime)   #6.016541957855225  # Therefore performance improved
