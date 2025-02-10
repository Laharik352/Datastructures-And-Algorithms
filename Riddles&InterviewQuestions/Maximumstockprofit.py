'''To find the maximum stock profit'''
#Case-1
def profit(stock_prices):
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]

    # Start off with a profit of zero
    max_profit = 0

    for price in stock_prices:
        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price, price)

        # Check the current price against our minimum for a profit
        # comparison against the max_profit
        comparison_profit = price - min_stock_price

        # Compare against our max_profit so far
        max_profit = max(max_profit, comparison_profit)

    return max_profit
# print(profit([10,12,14,12,13,11,8,7,6,13,23,45,11,10]))
# print(profit([30,22,21,5]))

#Case-2
def profit2(stock_prices):
    if len(stock_prices) < 2:
        raise Exception("Need a minimum of 2 values to compare")
    min_stock_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for price in stock_prices[1:]:
        comparison_profit = price - min_stock_price
        max_profit = max(comparison_profit, max_profit)
        # print("C",comparison_profit)
        # print("Max",max_profit)
        min_stock_price = min(min_stock_price, price)
        # print("Min",min_stock_price)
    return max_profit
# print(profit2([10,12,14,12,13,11,8,7,6,13,23,45,11,10]))
# print(profit2([1]))
print(profit2([30,22,21,5]))
