'''Creating a thread by extending thread class'''
# from threading import *
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Child Thread")
# t = MyThread()
# t.start()
# for i in range(10):
#     print("Main Thread")

'''Creating a thread without extending any class'''
from threading import *
class Test:
    def m1(self):
        for i in range(10):
            print("Child Thread")
obj = Test()
t = Thread(target=obj.m1)
t.start()
for i in range(10):
    print("Main Thread")