'''Selection sort algorithm'''
def selectionSort(l):
    for start in range(len(l)):
        print("Loop1", start)
        minpos = start
        for i in range(start, len(l)):
            print(i)
            print("l[i]", l[i])
            print("l[minpos]", l[minpos])
            if l[i] < l[minpos]:
                minpos = i
        (l[start], l[minpos]) = (l[minpos], l[start])
    return l
print(selectionSort([74, 32, 89, 55, 21, 64]))
# print(selectionSort(list(range(5000,0,-1))))

# '''Selection sort algorithm'''
# def selectionSort(l):
#     for start in range(len(l)):
#         print("Loop1", start)
#         minpos = start
#         for i in range(start, len(l)):
#             print(i)
#             print("l[i]", l[i])
#             print("l[minpos]", l[minpos])
#             if l[i] < l[start]:
#                 minpos = i
#                 (l[start], l[minpos]) = (l[minpos], l[start])
#     return l
# print(selectionSort([74, 32, 89, 55, 21, 64]))
# # print(selectionSort(list(range(5000,0,-1))))


