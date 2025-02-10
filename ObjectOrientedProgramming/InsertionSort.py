# '''Insertion sort Algorithm'''
# def InsertionSort(seq):
#     for sliceEnd in range(len(seq)):
#         pos = sliceEnd
#         # print("sliceEnd", sliceEnd)
#         # Build longer and longer sorted slices
#         #in each iteration seq[0:sliceEnd] already sorted
#         # Move the first element after the sorted slice left till it is in the correct place
#         while pos > 0 and seq[pos] < seq[pos -1]:
#             # print("pos", pos)
#             (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
#             pos = pos - 1
#             # print("pos1", pos)
#             # print(seq)
#     return seq
# print(InsertionSort([74, 32, 89, 55, 21, 64]))

'''Insertion sort using recursive function'''
def InsertionSort(seq):
    isort(seq, len(seq))
    return seq
def isort(seq,k):       #Sort slice seq[0:k]
    if k>1:
        # print('k', k)
        isort(seq, k-1)
        insert(seq, k-1)
        return seq
    else:
        return seq
def insert(seq, k):     # k starts from 2 and comparing takes place here...Inser seq[k] into sortedseq[0:k-1]
    # print('',seq)
    # print('k1', k)
    pos = k
    while pos > 0 and seq[pos] < seq[pos -1]:
        (seq[pos-1], seq[pos]) = (seq[pos], seq[pos - 1])
        pos = pos -1
        # print(seq)
    return seq
print(InsertionSort([74, 32, 89, 55, 21, 64]))