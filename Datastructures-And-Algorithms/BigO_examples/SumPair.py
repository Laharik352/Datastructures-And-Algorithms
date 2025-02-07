# Given an array of integers along with a number, find the UNIQUE pairs of numbers in the list that
#sum up to the given number
# from nose.tools import assert_equal
def sum_pair(lst, number):
    for i in range(0, len(lst)):        # this solution has Time complexity of O(n^2). So it is not reliable
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j] == number:
                t = lst[i],lst[j]
                print(t)
sum_pair([1,3,2,2],4)
sum_pair([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)

print("#################################")
def pair_sum(arr, k):       # this solution has a Time complexity of O(n)
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))
        # print("seen", seen)
        # print("output", output)
    # Nice one-liner for printing output
    # It converts each element in the tuple to list and each element in the list to type str and seperates the tuples with seperate lines
    return '\n'.join(map(str,list(output)))
print(pair_sum([1,3,2,2],4))
print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

