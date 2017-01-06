"""
Give solution for the 0/1 knapsack problem. That is given weights w1,w2,w3...wn and benefits b1,b2,b3,...,bn and maximum capacity of knapsack is M,
find the items that we will choose to maximize the benefit. You cannot take fractions of item you have to choose it or leave it.
"""

weight = [2, 3, 4, 5]
benefit = [3, 4, 5, 6]
capacity = 5


def knapsack01(weight, benefit, capacity):
    capacity += 1
    dp = [[0 for i in range(capacity)] for j in range(len(benefit))]
    for i in range(len(weight)):
        for j in range(capacity):
            if i == 0:
                if weight[i] <= j:
                    dp[i][j] = benefit[i]
            elif weight[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], benefit[i] + dp[i-1][j-weight[i]])
    elements = []
    i = len(weight)-1
    j = capacity - 1
    while i >= 0 and j >= 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            elements.append(weight[i])
            i -= 1
            j -= weight[i]
        if i < 0 or j < 0:
            break
    return dp[-1][-1], elements

res, elements = knapsack01(weight, benefit, capacity)
print(res)
print(elements)