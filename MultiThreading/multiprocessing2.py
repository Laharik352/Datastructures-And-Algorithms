# Here, we learn how to share data between two processes
import time
from multiprocessing import Process, Array, Value
# Every process has its own address space. THus program variables are not shared between two processes. You need to use interprocess
# communication(IPC) techniques if you want to share data between two processes.

def calc_square(arr, square_result, v):
    #Shared memory has different ways, we have to use enumerate
    print("calculating the square of numbers")
    v.value = 5.67
    for i, n in enumerate(arr):
        print('square:', n*n)
        square_result[i]=n*n
    print("Square result within the process:", square_result)

if __name__=='__main__':
    arr = [2,3,8,9]
    square_result = Array('i',4)   # Accessing the shared memory using Array: First argument is data type which is integer, second argument is size of the array
    v = Value('d', 0.0)     # Accessing the value in the shared memory
    p1 = Process(target=calc_square, args=(arr, square_result, v))     # We are accessing the shared memory using square_result

    p1.start()  # One process will appear in the task manager for each process, but this does not happen for a thread

    p1.join()

    print("Square result outside the process:", square_result[:]) # The filled variable square_result will not be able to be accessed by the main process since the added added is in the p1 process
    print("Done!")

    print(v.value)      # Printing the v.value initialized in the p1 process and accessing it in the main process