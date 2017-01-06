"""
Given coins of certain denominations and a total, how many ways these coins can be combined to get the total.
"""

coins = [1, 2, 3]
total = 5

def coin_change_ways(coins, total):
    total += 1
    dp = [[0 for i in range(total)] for j in range(len(coins))]
    for i in range(len(coins)):
        dp[i][0] = 1
    for i in range(len(coins)):
        for j in range(total):
            if i == 0:
                if j % coins[i] == 0:
                    dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
    print(dp)
    return dp[len(coins)-1][total-1]

print(coin_change_ways(coins, total))
