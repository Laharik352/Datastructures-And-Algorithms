'''active_count() and enumerate() Example'''
# from threading import *
# import time
# def display():
#     print(current_thread().name,"...started")
#     time.sleep(3)
#     print(current_thread().getName(),"...ended")
# print("The count of current number of threads", active_count()) #active_thread() used to get the total current thread numbers being executed
# t1 = Thread(target=display, name="ChildThread - 1")
# t2 = Thread(target=display, name="ChildThread - 2")
# t3 = Thread(target=display, name="ChildThread - 3")
# t1.start()
# t2.start()
# t3.start()
# print(t1.name, "is Alive", t1.isAlive())
# l = enumerate()     # To get the list of all the active threads running at this time
# for i in l:
#     print('Thread name:', i.name)
#     print("Thread Identification Number:", i.ident)
#     print()
# print("The count of current number of threads", active_count())
# time.sleep(10)
# print(t1.name, "is Alive", t1.isAlive())
# print("The count of current number of threads", active_count())

###############################################################################################################
'''join() method example'''
from threading import *
import time
def display():
    for i in range(10):
        print("Thread -1")
        time.sleep(3)
t = Thread(target=display)
t.start()
#t.join()            # Thread-1 telling thread-2 to wait until it completes all 10 iterations. Then thread-2 to start. Thread-2 agrees to wait until thread-1 has completed.
t.join(10)           # Thread-2 does not agree to wait for complete time and agrees to wait only for 10 seconds. After that thread-2 will start irrespective of thread-1 running or not.
for i in range(10):
    print("Thread -2")
