'''Implementation of counting sort
Create a function that takes in a list of unsorted prices (integers) and a maximum possible price value,
and return a sorted list of prices'''


def solution(unsorted_prices, max_price):
    # list of 0s at indices 0 to max_price
    prices_to_counts = [0] * (max_price + 1)
    # print(prices_to_counts)
    # populate prices
    for price in unsorted_prices:           #We are converting the unsorted list of elements in to a dictionary with key value pair
        # print(price)
        prices_to_counts[price] += 1

    # print(dict(enumerate(prices_to_counts)))

    # populate final sorted prices
    sorted_prices = []

    # For each price in prices_to_counts
    for price, count in enumerate(prices_to_counts):        # enumerate similar to price_to_counts.getitems()

        # for the number of times the element occurs
        for time in range(count):
            # add it to the sorted price list
            sorted_prices.append(price)

    return sorted_prices

print(solution([4,6,2,2,7,3,8,9],9))
print(solution([4,6,2,7,3,8,9],9))