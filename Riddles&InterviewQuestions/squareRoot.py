'''Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function.
For example, squareroot of a number between [9, 15] should return 3, and [16, 24] should be 4.'''
#Solution-1
def solution(num):
    if num<0:
        raise ValueError
    if num==1:
        return 1
    for k in range((num//2)+1): # Adding 1 since the range is from 0
        if k**2==num:
            return k
        elif k**2>num:
            return k-1
    return k
print(solution(14))
print(solution(15))
print(solution(16))


#Solution-2: Using recursion
def better_solution(num):
    if num < 0:
        raise ValueError
    if num == 1:
        return 1
    low = 0
    high = 1 + (num // 2)

    while low+1 < high:       #
        #mid = low + (high - low) // 2
        mid = (low+high)//2
        square = mid ** 2
        if square == num:
            return mid
        elif square < num:
            low = mid
        else:
            high = mid

    return low
print(better_solution(14))
print(better_solution(15))
print(better_solution(16))