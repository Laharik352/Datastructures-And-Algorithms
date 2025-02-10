from multiprocessing import Pool
import time
# When you are using pool, then you are speeding up the tasks between since you are equally dividing the entire task equally among all the CPU processors
def f(n):
    sum = 0
    for x in range(1000):
        sum+=x*x
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    # p = Pool(processes=3)       # Here you divide the work only between 3 processors even if your system has 8 processors
    result = p.map(f, range(1000))
    p.close()
    p.join()
    print("Pool took: ", time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))

    print("Serial processing: ", time.time()-t2)
