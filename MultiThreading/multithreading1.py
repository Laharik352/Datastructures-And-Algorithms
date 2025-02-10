import time
from threading import Thread

# def calc_square(arr):
#     print("calculating the square of numbers")
#     for i in arr:
#         time.sleep(0.2) # During this time, the CPU will be idle, so we need to utilize this time and make the CPU do some task. THis can be done with the help of multithreading
#         print('square:', i*i)
#
# def calc_cube(arr):
#     print("calculating the cube of numbers")
#     for i in arr:
#         time.sleep(0.2)
#         print('cube:', i*i*i)
#
# arr = [2,3,8,9]
#
# t = time.time()
# calc_square(arr)
# calc_cube(arr)
#
# print("done in: ", time.time()-t)
# print("I'm done with all my work now!!")


def calc_square(arr):
    print("calculating the square of numbers")
    for i in arr:
        time.sleep(0.2) # During this time, the CPU will be idle, so we need to utilize this time and make the CPU do some task. THis can be done with the help of multithreading
        print('square:', i*i)

def calc_cube(arr):
    print("calculating the cube of numbers")
    for i in arr:
        time.sleep(0.2)
        print('cube:', i*i*i)

arr = [2,3,8,9]

t = time.time()
t1 = Thread(target=calc_square, args=(arr,)) #target is the task like calculate square, cube etc. args is the arguments for the task
t2 = Thread(target=calc_cube, args=(arr,))  # Since args is being passed as a tuple, we need to put a ","

t1.start()  # To start the thread
t2.start()  # During the 0.2 seconds, the t2 thread will run

t1.join() # when join() is used for a particular thread the main thread will stop executing until the execution of joined thread is complete.
t2.join()

print("done in: ", time.time()-t)
print("I'm done with all my work now!!")

