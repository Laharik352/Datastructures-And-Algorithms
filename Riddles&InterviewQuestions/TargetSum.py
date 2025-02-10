'''Given a list of integers and a target number, write a function that returns a boolean indicating if
its possible to sum two integers from the list to reach the target number'''

def solution(lst, target):
    # Create set to keep track of duplicates
    seen = set()

    # We want to find if there is a num2 that sums with num to reach the target

    for num in lst:

        num2 = target - num

        if num2 in seen:
            return True

        seen.add(num)

    # If we never find a pair match which creates the sum
    return False
print(solution([1,3,5,1,7],4))
print(solution([1,3,5,1,7],14))
