'''Example of Quadratic functions O(n**2)'''
def func_quad(lst):
    for item1 in lst:       # We're going through each item twice here.
        for item2 in lst:   # 2 loops, for n items...we have to perform n operation (n*n=n**2)
            print(item1, item2)
lst = [1,2,3]
func_quad(lst)      # So if we have 10 items in the list, we'll have 10**2==100 operations printed. So, it will be dangerous for large inputs