# Multiprocessing: Here, we create two processes one to calculate the square of two numbers and another to calculate the cube of two numbers
import time
from multiprocessing import Process
# Every process has its own address space. THus program variables are not shared between two processes. You need to use interprocess
# communication(IPC) techniques if you want to share data between two processes.

square_result = []
def calc_square(arr):
    global square_result
    print("calculating the square of numbers")
    for i in arr:
        print('square:', i*i)
        square_result.append(i*i)
    print("within the process:", square_result)

def calc_cube(arr):
    print("calculating the cube of numbers")
    for i in arr:
        print('cube:', i*i*i)

if __name__=='__main__':
    arr = [2,3,8,9]
    p1 = Process(target=calc_square, args=(arr,))
    p2 = Process(target=calc_cube, args=(arr,))

    p1.start()  # One process will appear in the task manager for each process, but this does not happen for a thread
    p2.start()

    p1.join()
    p2.join()

    print("Square result:", str(square_result)) # The filled variable square_result will not be able to be accessed by the main process since the added added is in the p1 process
    print("Done!")