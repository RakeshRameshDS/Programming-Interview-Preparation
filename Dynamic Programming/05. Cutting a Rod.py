"""
Given a rod of length N units and price of rods of all sizes from 1 to N, find the best way of cutting the rod,
i.e in how many pieces and of what length we should cut so that we get maximum price for it.
"""

length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]

def max_price_rod(length, price, req):
    dp = [[0 for i in range(req+1)] for j in range(len(length))]
    for i in range(len(length)):
        for j in range(req+1):
            if length[i] > j:
                if i > 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] = max(dp[i-1][j], price[i] + dp[i][j-length[i]])
                else:
                    dp[i][j] = price[i] + dp[i][j-length[i]]
    sel = []
    i = len(length)-1
    j = req
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            sel.append(length[i])
            j -= length[i]
    return sel, dp[-1][-1]

res = max_price_rod(length, price, 20)
print("RES - ", res[1])
print("Selected - ", res[0])
