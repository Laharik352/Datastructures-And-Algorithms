# '''Fibonacci numbers using generators'''
# def fib():          # WHerever large volumes of data is available, then we go for generators
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b, a+b
# for n in fib():
#     if n>100:
#         break
#     print(n)


'''Performance improvement using generators'''   # (i)Performance and (ii)memory utilization is going to increase (iii)Generators are easy to use when compared to lists
                                                 # (iv) Highly used for web scraping
'''Case-1: Without using generator'''       # More time taken
import random
import time
names = ['sunny', 'bunny', 'kunny']
subjects = ['Python', "java", 'javascript']
def people_list(num):
    results = []
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject':random.choice(subjects)
        }
        results.append(person)
    return results

t1 = time.process_time()
people = people_list(100000)
t2 = time.process_time()
print('Time taken for list:', t2-t1)

'''Case-2: With using generators'''         # Very less time taken
import random
import time
names = ['sunny', 'bunny', 'kunny']
subjects = ['Python', "java", 'javascript']
def people_generator(num):
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject':random.choice(subjects)
        }
        yield person

t1 = time.process_time()
people = people_generator(100000)
t2 = time.process_time()
print('Time taken for generators:', t2-t1)

