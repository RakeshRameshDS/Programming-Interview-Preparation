"""
Given coins of denomination v1=1,v2,v3,v4,...,vn in ascending order find minimum number of coins required to make an amount P.
"""

total = 13
coins = [7, 2, 3, 6]
holder = {}  # Global variable to hold optimal sub problem results
contents = {}

def min_coins_rec(coins, total):
    global holder, contents
    if total in holder:
        return holder[total]
    if total < 0:
        return 999
    elif total == 0:
        return 0
    else:
        min_val = 9999
        selected_coin = -1
        for coin in coins:
            val = min_coins_rec(coins, total - coin) + 1
            if val < min_val:
                min_val = val
                selected_coin = coin
        holder[total] = min_val
        contents[total] = selected_coin
        return min_val


print(min_coins_rec(coins, total))
print(contents)
coin_vals = []
res = total
while res != 999 and res > 0:
    x = contents[res]
    coin_vals.append(x)
    res = total - x
    total = res
print(coin_vals)