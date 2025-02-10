# '''Worst case and best case in Linear notation of big(0)'''
# def Lin(lst, match):
#     for item in lst:
#         if item == match:
#             return True
#     return False
# lst = [1,2,3,4,5,6,7,8,9,10,11]
# print(Lin(lst,1))   # This is the best case and bigO is O(1)
# print(Lin(lst,12))  # THis is the worst case and bigO is O(n)


# Space Complexity for linear functions - Space complexity is the space/memory the function occupies
#Here the time complexity is linear O(n)
#Space complexity is also linear - for each time, the function adds a new object 'new' into the list thereby increasing the memory linearly
def create_list(n):
    nl = []
    for i in range(n):
        nl.append('new')
    return nl
print(create_list(5))

#For the below function, the time complexity is linear 0(n)
# But the space complexity is constant- O(1) because each time, the same "Hello world" is itself getting printed, so no new memory gets allocated
def printer(x):
    for i in range(x):
        print("Hello world")
printer(10)