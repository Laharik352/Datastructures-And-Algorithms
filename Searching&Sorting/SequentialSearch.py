'''Sequential search for unordered lists'''
def SeqSearch(arr, elem):
    for element in range(len(arr)):
        if element == elem:
            found = True
        else:
            found = False
    return found
print(SeqSearch([1,3,2,5,4], 4))
print(SeqSearch([1,3,2,5,4], 6))

'''Sequential search for ordered lists'''
def SeqSearchOrdered(arr, elem):
    for element in range(len(arr)):
        if element == elem:
            found = True
        else:
            if arr[element] > elem:
                stopped = True
            found = False
    return found
print(SeqSearchOrdered([1,2,3,4,5], 4))
print(SeqSearchOrdered([1,2,3,4,5], 6))
