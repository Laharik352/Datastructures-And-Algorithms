'''Unsorted case: Go through each element and search for the required element'''
# def search(seq, v):
#     for x in seq:
#         if x == v:
#             # print(x)
#             return ("{} found".format(v))
#     return("ELement not found")
# print(search([2,6,6,4],6))

# dont refer this
# def search(seq, v):
#     for i in range(len(seq)):
# def search(seq, v):
#     for x in seq:
#         if x == v:
#             print(x)
#             print("{} found".format(v))
#     print("ELement not found")
# search([2,6,6,4],6)

#'''Sorted case: Bunary search'''
def bsearch(seq, v, l, r):
    if (r-l)==0:
        return False
    mid = (r+l)//2          #integer devision
    if (v == seq[mid]):
        return True
    if (v < seq[mid]):
        return (bsearch(seq, v, l, mid))
    else:
        return (bsearch(seq, v, mid+1, r))
print(bsearch([1,2,3,4,5], 4, 1,5))