# # '''Example-1'''
# import threading
# print("Current Executing thread:", threading.current_thread().getName())  # How to get the name of the current thread
# threading.current_thread().setName("My thread")                           # How to set the name of the current thread to your own name
# print("Current Executing thread:", threading.current_thread().getName())  # You can also use threading.current_thread().name

########################################################################################################################################
'''Thread Identification Number: Every thread has a unique identification number during its execution'''
from threading import *
def test():
    print("Child thread")
t = Thread(target=test)
t.start()
print("Main Thread Identification number:", current_thread().ident)     #'ident' used for getting the Thread Identification Number of a thread
print("Child Thread Identification Number:", t.ident)

########################################################################################################################################
'''Problem: Creating a thread without using class'''
# from threading import *     #threading is the module name
# def display():
#     for i in range(10):
#         print("Child Thread")
# t = Thread(target=display)      #Thread is the name of the class predefined in the threading module and t is the object
# t.start()
# for i in range(10):
#     print("Main thread")

########################################################################################################################################
'''Problem: You want to print "Hello World" 20 times'''
# from threading import *     #threading is the module name
# def display():
#     for i in range(10):
#         print("Hello World")
# t = Thread(target=display)      #Thread is the name of the class predefined in the threading module and t is the object
# t.start()
# for i in range(10):
#     print("Hello World")        # Here ten ten times individually you are printing hello world, this is much faster than making the main thread to print hello world 20 times

########################################################################################################################################
# from threading import *     #threading is the module name
# def display():
#     for i in range(10):
#         print("Child Thread:", current_thread().getName())
# t = Thread(target=display)      #Thread is the name of the class predefined in the threading module and t is the object
# t.start()
# for i in range(10):
#     print("Main thread:", current_thread().getName())
