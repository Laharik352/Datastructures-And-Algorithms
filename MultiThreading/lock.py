import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()      # To put a lock
        balance.value = balance.value+1
        lock.release()      # To release the lock

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()      # The two lines 8 and 15 is called the critical section. We have to use lock.acquire and lock.release around the critical section
        balance.value = balance.value-1     # Whatever part of the code that is used to access the shared resource is called the critical section
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    # To avoid erraneous results, we create a lock here
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))
    d.start()
    w.start()
    d.join()    
    w.join()
    print(balance.value) # To avoid erraneous results, we create a lock
