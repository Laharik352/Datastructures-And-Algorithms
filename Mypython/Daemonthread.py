'''example - 1'''
# from threading import *
# mt = current_thread()
# print(mt.isDaemon())           # To check if the thread is Daemon or not...Main thread is not Daemon thread
# print(mt.daemon)
# mt.setDaemon(True)             # this will not work since the main thread has already started
# print(mt.daemon)

# ###############################################################################################
# from threading import *
# def job():
#     print("executed child thread")
# t = Thread(target=job)  # This thread is created by main thread which is non-Daemon and is the parent. So, the t will also be Non-Daemon
# print(t.isDaemon())     # To check the daemon nature of the thread......False
# t.setDaemon(True)       # To set the daemon nature of the thread. You can do this since the thread has not yet started. IF the thread has started, then you cannot change the nature.
# print(t.daemon)         # To check the daemon nature of the thread

###############################################################################################
'''
from threading import *             # The Daemon nature is always inherited from the parent to child
import time
def job1():
    print("executed by t1")
    t2 = Thread(target=job2)
    print("Nature of t2:", t2.isDaemon())   #Parent is t1 which is Daemon thread. So, this is also a Daemon thread.
    t2.start()
def job2():
    print("executed by t2")
t1 = Thread(target=job1)        # Here parent is main thread which is non-daemon
print("Nature of t1:", t1.isDaemon())   #False
t1.setDaemon(True)
print("Nature of t1:", t1.isDaemon())   #Now it is True
t1.start()
time.sleep(10)

"""     Main
        ___|____
       |        |
    Main        t1
      |       ___|____
      |       |       |
    Main      t1      t2"""     # Total three threads
'''

###############################################################################################
# from threading import * #Here both main and t are Non-Daemon. so each will continue to execute until their completion
# import time
# def job():
#     for i in range(10):
#         print("Lazy thread")
#         time.sleep(2)
#
# t = Thread(target=job)
# t.start()
# time.sleep(10)
# print("End of main thread")

##############################################################################################
from threading import *        # Here t is Daemon thread and Main thread is Non Daemon. So, when main thread completes execution, then the t thread will also stop even it has not completed.
import time                    # THis is because, the Daemon thread is only a supporting thread, when Non-Daemon thread stops...no use of Daemon thread, it will also stop.
def job():
    for i in range(10):
        print("Lazy thread")
        time.sleep(2)

t = Thread(target=job)
t.setDaemon(True)
t.start()
time.sleep(10)
print("End of main thread")