# Here, we learn how to share data between two processes
# Here we use queue to access the data between two process
import time
from multiprocessing import Process, Array, Value, Queue
# Every process has its own address space. THus program variables are not shared between two processes. You need to use interprocess
# communication(IPC) techniques if you want to share data between two processes.

def calc_square(arr, q):
    print("calculating the square of numbers")
    for n in arr:
        print('square:', n*n)
        q.put(n*n)


if __name__=='__main__':
    arr = [2,3,8,9]
    q = Queue()
    p1 = Process(target=calc_square, args=(arr, q))     # We are accessing the shared memory using square_result

    p1.start()  # One process will appear in the task manager for each process, but this does not happen for a thread
    p1.join()

    while q.empty() is False:
        print(q.get())