'''Write a function that given a target amount of money and a list of possible coin denominations. Write a funtion that
returns the number of ways to make change for the target amount using the coin denominations'''

def solution(n, coins):

    # Set up our array for trakcing results
    arr = [1] + [0] * n
    print(arr)

    for coin in coins:
        # print("coin", coin)
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
            # print(arr[i])

    if n == 0:
        return 0
    else:
        return arr[n]

print(solution(10, [1, 2, 3]))