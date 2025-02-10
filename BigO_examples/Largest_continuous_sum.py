'''In this problem, you have to find the largest continuous sum'''
def large_cont_sum(arr):
    current_sum = max_sum = arr[0]
    for num in arr[1: ]:
        current_sum = max(current_sum+num, num)
        #current_sum = current_sum + num
        max_sum = max(current_sum, max_sum)
    return max_sum
print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))