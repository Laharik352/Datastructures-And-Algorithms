'''Implementation of generators'''
#Advantages: 1)generators do not require the entire result set to be constructed all at once like the list comprehension. Hence, optimizes the memory space
#            2) The entire result production is divided into smaller intervals. Hence a programmer doesn't have to wait for the entire result set to be constructed at once.
# without generators
def square_number(nums):
    result = []         # here, we have this list store the values and return it when needed
    for i in nums:
        result.append(i*i)
    return result
print(square_number([1,2,3,4,5]))

#With generators
def square_numbers(nums):
    for i in nums:
        yield i*i
for i in square_numbers([1,2,3,4,5]):       #First way of getting the values
    print(i)

mynums = square_numbers([1,2,3,4,5])        #Second way of fetching the values
print(next(mynums))                         # At runtime we are generating the values and printing them, this improves memory utilization
print(next(mynums))                         # The next method returns the next item in the iteration until all the items are over after whcih it throws a stop iteration error
print(next(mynums))
print(next(mynums))
print(next(mynums))

# Generators using tuples-----> GENERATOR EXPRESSIONS
my_nums = (x*x for x in [1,2,3,4,5])         # By putting () instead of [], we internally use generators, this is called a generator expression
print(my_nums)
for i in my_nums:
    print(i)
print(list(my_nums))            # When you do this, you will lose the advantages of using generators
                                # Here, when we have 100s of values, then it will take a lot of memory and decreases the performance


