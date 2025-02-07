'''Missing element problem: In this problem, there will be 2 arrays given. The first array will be the main one.
The second array will be shuffled and will have missing elements. We need to find the missing elements in the second array'''
def missing_element(array1, array2):
    for i in range(len(array1)):    # THis approach is O(n^2)
        if array1[i] not in array2:
            print(array1[i])
missing_element([1,2,3,4,5],[2,1,4,3])

# Solution using dictionaries
import collections
def finder(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2:                # This is O(NlogN)
        d[num] += 1
    # print(d)
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
    # print(d)
print(finder([1,2,3,4,5],[1,2,4,3]))

#find the sum of the first array and subtract the sum of the second array sum from the first one, the missing element is the difference
def finder1(arr1, arr2):
    sum = 0
    for num in range(len(arr1)):    # This is O(N)
        sum += arr1[num]
    for num in range(len(arr2)):
        sum -= arr2[num]
    return sum
print(finder1([1,2,3,4,5],[2,1,4,3]))


#Perform an XOR between the numbers in the 2 arrays
def finder2(arr1, arr2):
    # print(arr1+arr2)
    result = 0
    for num in arr1+arr2:
        result^=num
    return result
print(finder2([1,2,3,4,5],[2,1,4,3]))
