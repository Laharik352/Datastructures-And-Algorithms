'''Find the cumilative sum of numbers'''
def cum_sum(n):
    if n == 0:
        return 0
    else:
        return n+cum_sum(n-1)
print(cum_sum(5))